# pylint: disable=unused-argument, import-error, too-many-arguments
# pylint: disable=unnecessary-comprehension, no-member, no-name-in-module

"""
draft.py
==============

Draft screen

"""

from functools import partial
import time
import os

from kivy.clock import Clock
from kivy.properties import (
    ListProperty,
    StringProperty
)
from kivy.uix.screenmanager import Screen
from kivy.app import App

import state

from bitmessagekivy import kivy_helper_search
from bitmessagekivy.baseclass.common import (
    showLimitedCnt, toast, ThemeClsColor, empty_screen_label,
    SwipeToDeleteItem, ShowTimeHistoy, mdlist_message_content
)
from bitmessagekivy.baseclass.maildetail import MailDetail

from addresses import decodeAddress
from bmconfigparser import config

import helper_sent
from debug import logger


class Draft(Screen):
    """Draft screen class for kivy Ui"""

    data = ListProperty()
    account = StringProperty()
    queryreturn = ListProperty()
    has_refreshed = True
    label_str = "yet no message for this account!!!!!!!!!!!!!"

    def __init__(self, *args, **kwargs):
        """Method used for storing draft messages"""
        super(Draft, self).__init__(*args, **kwargs)
        self.kivy_running_app = App.get_running_app()
        self.kivy_state = self.kivy_running_app.kivy_state_obj
        if self.kivy_state.association == '':
            if state.kivyapp.variable_1:
                self.kivy_state.association = state.kivyapp.variable_1[0]
        Clock.schedule_once(self.init_uip, 0)

    def init_ui(self, dt=0):
        """Clock Schdule for method draft accounts"""
        self.sent_accounts()
        logger.debug(dt)

    def sent_accounts(self):
        """Load draft accounts"""
        self.load_draft()

    def load_draft(self, where="", what=""):
        """Load draft list for Draft messages"""
        self.account = self.kivy_state.association
        xAddress = 'fromaddress'
        self.ids.tag_label.text = ''
        self.draft_data_query(xAddress, where, what)
        if self.queryreturn:
            self.ids.tag_label.text = 'Draft'
            self.set_draft_count(self.kivy_state.draft_count)
            self.set_mdList()
            self.ids.scroll_y.bind(scroll_y=self.check_scroll_y)
        else:
            self.set_draft_count('0')
            self.ids.ml.add_widget(empty_screen_label(self.label_str))

    def draft_data_query(self, xAddress, where, what, start_indx=0, end_indx=20):
        """Retrieve draft messages"""
        self.queryreturn = kivy_helper_search.search_sql(
            xAddress, self.account, "draft", where, what,
            False, start_indx, end_indx)

    @staticmethod
    def set_draft_count(Count):
        """Set the count of draft mails"""
        draftCnt_obj = state.kivyapp.root.ids.content_drawer.ids.draft_cnt
        draftCnt_obj.ids.badge_txt.text = showLimitedCnt(int(Count))

    def set_mdList(self):
        """Create mdlist of messages"""
        data = []
        total_draft_msg = len(self.ids.ml.children)
        mdlist_message_content(self.queryreturn, data=data)
        for item in data:
            message_row = SwipeToDeleteItem(
                text='Draft',
            )
            listItem = message_row.ids.content
            listItem.secondary_text = item["text"]
            listItem.theme_text_color = "Custom"
            listItem.text_color = ThemeClsColor
            message_row.ids.avater_img.source = os.path.join(state.imageDir, 'avatar.png')
            listItem.bind(on_release=partial(
                self.draft_detail, item['ackdata'], message_row))
            message_row.ids.time_tag.text = str(ShowTimeHistoy(item['senttime']))
            message_row.ids.delete_msg.bind(on_press=partial(self.delete_draft, item['ackdata']))
            self.ids.ml.add_widget(message_row)
        updated_msg = len(self.ids.ml.children)
        self.has_refreshed = True if total_draft_msg != updated_msg else False

    def check_scroll_y(self, instance, somethingelse):
        """Load data on scroll"""
        if self.ids.scroll_y.scroll_y <= -0.0 and self.has_refreshed:
            self.ids.scroll_y.scroll_y = 0.06
            total_draft_msg = len(self.ids.ml.children)
            self.update_draft_screen_on_scroll(total_draft_msg)

    def update_draft_screen_on_scroll(self, total_draft_msg, where='', what=''):
        """Load more data on scroll down"""
        self.draft_data_query('fromaddress', where, what, total_draft_msg, 5)
        self.set_mdList()

    def draft_detail(self, ackdata, instance, *args):
        """Set draft Details"""
        if instance.state == 'closed':
            instance.ids.delete_msg.disabled = True
            if instance.open_progress == 0.0:
                self.kivy_state.detailPageType = 'draft'
                self.kivy_state.mail_id = ackdata
                if self.manager:
                    src_mng_obj = self.manager
                else:
                    src_mng_obj = self.parent.parent
                src_mng_obj.screens[11].clear_widgets()
                src_mng_obj.screens[11].add_widget(MailDetail())
                src_mng_obj.current = 'mailDetail'
        else:
            instance.ids.delete_msg.disabled = False

    def delete_draft(self, data_index, instance, *args):
        """Delete draft message permanently"""
        helper_sent.delete(data_index)
        if int(self.kivy_state.draft_count) > 0:
            self.kivy_state.draft_count = str(int(self.kivy_state.draft_count) - 1)
            self.set_draft_count(self.kivy_state.draft_count)
            if int(self.kivy_state.draft_count) <= 0:
                self.ids.tag_label.text = ''
        self.ids.ml.remove_widget(instance.parent.parent)
        toast('Deleted')

    @staticmethod
    def draft_msg(src_object):
        """Save draft mails"""
        composer_object = state.kivyapp.root.ids.sc3.children[1].ids
        fromAddress = str(composer_object.ti.text)
        toAddress = str(composer_object.txt_input.text)
        subject = str(composer_object.subject.text)
        message = str(composer_object.body.text)
        encoding = 3
        sendMessageToPeople = True
        if sendMessageToPeople:
            ripe = decodeAddress(toAddress)[2:]
            from addresses import addBMIfNotPresent
            toAddress = addBMIfNotPresent(toAddress)
            helper_sent.insert(
                toAddress=toAddress,
                fromAddress=fromAddress,
                subject=subject,
                message=message,
                status='msgqueued',
                ripe=ripe,
                sentTime=int(time.time()),
                lastActionTime=int(time.time()),
                sleeptill=0,
                retryNumber=0,
                encoding=encoding,
                ttl=config.safeGetInt('bitmessagesettings', 'ttl'),
                folder='draft',
            )
            Draft().kivy_state.draft_count = str(int(Draft().kivy_state.draft_count) + 1) \
                if Draft().kivy_state.association == fromAddress else Draft().kivy_state.draft_count
            src_object.ids.sc16.clear_widgets()
            src_object.ids.sc16.add_widget(Draft())
            toast('Save draft')
        return
