# pylint: disable=too-many-arguments, no-name-in-module, import-error
# pylint: disable=too-few-public-methods, no-member

"""
MyAddress widgets are here.
"""

from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel
from kivymd.uix.list import IRightBodyTouch

import state

from bitmessagekivy.get_platform import platform
from bitmessagekivy.baseclass.common import ThemeClsColor


class BadgeText(IRightBodyTouch, MDLabel):
    """BadgeText class for kivy UI"""


# pylint: disable=no-init, old-style-class
class DefaultLabelMixin:
    """Widget used in MyAddress are here"""

    @staticmethod
    def default_label_when_empty():
        """This function returns default message when no address is generated."""
        empty_search_label = "No address found!"
        no_address_found = "yet no address is created by user!!!!!!!!!!!!!"
        content = MDLabel(
            font_style='Caption',
            theme_text_color='Primary',
            text=empty_search_label if state.searching_text  # FIXME: Need to replace state with kivy_state
            else no_address_found, halign='center', size_hint_y=None, valign='top')
        return content


class HelperMyAddress(DefaultLabelMixin):
    """Widget used in MyAddress are here"""

    @staticmethod
    def is_active_badge():
        """This function show the 'active' label of active Address."""
        badge_obj = BadgeText(
            size_hint=(None, None),
            size=[90 if platform == 'android' else 50, 60],
            text='Active', halign='center',
            font_style='Body1', theme_text_color='Custom',
            text_color=ThemeClsColor, font_size='13sp'
        )
        return badge_obj

    @staticmethod
    def myaddress_detail_popup(obj, width):
        """This method show the details of address as popup opens."""
        show_myaddress_dialogue = MDDialog(
            type="custom",
            size_hint=(width, .25),
            content_cls=obj,
        )
        return show_myaddress_dialogue

    @staticmethod
    def inactive_address_popup(width, callback_for_menu_items):
        """This method shows the warning popup if the address is inactive"""
        dialog_text = 'Address is not currently active. Please click on Toggle button to active it.'
        dialog_box = MDDialog(
            text=dialog_text,
            size_hint=(width, .25),
            buttons=[
                MDFlatButton(
                    text="Ok", on_release=lambda x: callback_for_menu_items("Ok")
                ),
            ],
        )
        return dialog_box
