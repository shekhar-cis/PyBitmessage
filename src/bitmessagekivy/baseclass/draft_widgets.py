# pylint: disable=no-member, too-many-arguments
"""
Draft screen widgets are here.
"""


from kivymd.uix.button import MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel

import state


class HelperDraft(object):
    """Widget used in Draft screen are here"""
    def __init__(self):
        pass

    # @staticmethod
    # def default_label_when_empty():
    #     """This function returns default message while no address is there."""
    #     empty_screen_msg = "yet no message for this account!!!!!!!!!!!!!"
    #     content = MDLabel(
    #         font_style='Caption',
    #         theme_text_color='Primary',
    #         text=empty_screen_msg,
    #         halign='center',
    #         size_hint_y=None,
    #         valign='top')
    #     return content
