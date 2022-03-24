# pylint: disable=no-member, too-many-arguments
"""
MyAddress widgets are here.
"""
from bitmessagekivy.get_platform import platform

from kivymd.uix.button import MDRaisedButton
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel
from kivymd.uix.list import (IRightBodyTouch, TwoLineAvatarIconListItem)

import state

from bitmessagekivy.baseclass.common import (
    avatarImageFirstLetter, AvatarSampleWidget, ThemeClsColor,
    toast
)

class BadgeText(IRightBodyTouch, MDLabel):
    """BadgeText class for kivy Ui"""

class HelperMyAddress(object):
    """Widget used in MyAddress are here"""
    def __init__(self):
        pass

    @staticmethod
    def default_label_when_empty():
        """This function returns default message when no address is generated."""
        content = MDLabel(
            font_style='Caption',
            theme_text_color='Primary',
            text="No address found!" if state.searching_text
            else "yet no address is created by user!!!!!!!!!!!!!", halign='center', size_hint_y=None, valign='top')
        return content

    @staticmethod
    def is_active_badge():
        badge_obj = BadgeText(
            size_hint=(None, None),
            size=[90 if platform == 'android' else 50, 60],
            text='Active', halign='center',
            font_style='Body1', theme_text_color='Custom',
            text_color=ThemeClsColor, font_size = '13sp'
        )
        return badge_obj

    @staticmethod
    def myaddress_detail_popup(obj, width):
        show_myaddress_dialogue = MDDialog(
            type="custom",
            size_hint=(width, .25),
            content_cls=obj,
        )
        return show_myaddress_dialogue

    @staticmethod
    def inactive_address_popup(width, callback_for_menu_items):
        dialog_box = MDDialog(
            text='Address is not currently active. Please click on Toggle button to active it.',
            size_hint=(width, .25),
            buttons=[
                MDFlatButton(
                    text="Ok", on_release=lambda x: callback_for_menu_items("Ok")
                ),
            ],
        )
        return dialog_box
