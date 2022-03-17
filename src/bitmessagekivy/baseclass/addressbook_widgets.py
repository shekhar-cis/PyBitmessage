import state

from bitmessagekivy.get_platform import platform

from kivymd.uix.button import MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel

from bitmessagekivy.baseclass.popup import AddbookDetailPopup


class HelperAddressBook(object):
    """Widget used in Addressbook are here"""

    @staticmethod
    def default_label_when_empty():
            content = MDLabel(
                font_style='Caption',
                theme_text_color='Primary',
                # TODO: searcing_text(typo) need to create a kivy_state.py and add kivy related variables
                text="No contact found!" if state.searcing_text
                else "No contact found yet...... ", halign='center', size_hint_y=None, valign='top')
            return content

    @staticmethod
    def address_detail_popup(obj, send_message, update_address, close_popup, width):
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
    
    @staticmethod
    def compose_message(from_addr=None, to_addr=None, subject=None, body=None): 
        window_obj = state.kivyapp.root.ids
        if to_addr:
            window_obj.sc3.children[1].ids.txt_input.text = to_addr
        if from_addr:
            window_obj.sc3.children[1].ids.txt_input.text = from_addr
        window_obj.sc3.children[1].ids.ti.text = ''
        window_obj.sc3.children[1].ids.btn.text = 'Select'
        window_obj.sc3.children[1].ids.subject.text = ''
        window_obj.sc3.children[1].ids.body.text = ''
        window_obj.scr_mngr.current = 'create'
