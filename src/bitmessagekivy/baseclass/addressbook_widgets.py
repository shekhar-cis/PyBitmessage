import state

from bitmessagekivy.get_platform import platform

from kivymd.uix.button import MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel

from bitmessagekivy.baseclass.popup import AddbookDetailPopup


class HelperAddressBook:
    """Widget used in Addressbook are here"""

    @staticmethod
    def default_label_when_empty():
            content = MDLabel(
                font_style='Caption',
                theme_text_color='Primary',
                # TODO: searcing_text(typo), need to create a kivy_state.py and add kivy related variables
                text="No contact found!" if state.searcing_text
                else "No contact found yet...... ",
                halign='center',
                size_hint_y=None,
                valign='top')
            return content

    def address_detail_popup(self, send_message, update_address, close_popup, width, obj):
        retval = MDDialog(
                    type="custom",
                    size_hint=(width, .25),
                    content_cls=obj,
                    buttons=[
                        MDRaisedButton(
                            text="Send message to",
                            on_release=send_message,
                        ),
                        MDRaisedButton(
                            text="Save",
                            on_release=update_address,
                        ),
                        MDRaisedButton(
                            text="Cancel",
                            on_release=close_popup,
                        ),
                    ],
                )
        return retval