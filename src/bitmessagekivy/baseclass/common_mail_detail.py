# pylint: disable=no-name-in-module, attribute-defined-outside-init, import-error
"""
    All Common widgets of kivy are managed here.
"""

from datetime import datetime

from kivy.core.window import Window
from kivy.metrics import dp
from kivy.uix.image import Image
from kivy.properties import (
    NumericProperty,
    StringProperty
)
from kivy.app import App

from kivymd.uix.list import (
    ILeftBody,
    IRightBodyTouch,
)
from kivymd.uix.label import MDLabel
from kivymd.toast import kivytoast
from kivymd.uix.card import MDCardSwipe
from kivymd.uix.chip import MDChip

from bitmessagekivy.get_platform import platform

from bitmessagekivy.baseclass.maildetail import MailDetail
from bitmessagekivy.baseclass.common import kivy_state_variables


def mail_detail_screen(screen_name, msg_id, instance, folder, *args):
    kivy_state = kivy_state_variables()
    if instance.open_progress == 0.0:
        import pdb; pdb.set_trace()
        kivy_state.detailPageType = folder
        kivy_state.mail_id = msg_id
        if screen_name.manager:
            src_mng_obj = screen_name.manager
        else:
            src_mng_obj = screen_name.parent.parent
        src_mng_obj.screens[11].clear_widgets()
        src_mng_obj.screens[11].add_widget(MailDetail())
        src_mng_obj.current = "mailDetail"
