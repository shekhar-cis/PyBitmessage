import state

from bitmessagekivy.get_platform import platform

from kivymd.uix.button import MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel

from bitmessagekivy.baseclass.popup import AddbookDetailPopup

class HelperAddressBook:
    def default_label_while_empty():
            content = MDLabel(
                font_style='Caption',
                theme_text_color='Primary',
                text="No contact found!" if state.searcing_text
                else "No contact found yet...... ",
                halign='center',
                size_hint_y=None,
                valign='top')
            return content

    def address_detail_popup(self, address, label, instance):
                obj = AddbookDetailPopup()
                self.address_label = obj.address_label = label
                self.address = obj.address = address
                width = .9 if platform == 'android' else .8
                self.addbook_popup = MDDialog(
                    type="custom",
                    size_hint=(width, .25),
                    content_cls=obj,
                    buttons=[
                        MDRaisedButton(
                            text="Send message to",
                            on_release=self.send_message_to,
                        ),
                        MDRaisedButton(
                            text="Save",
                            on_release=self.update_addbook_label,
                        ),
                        MDRaisedButton(
                            text="Cancel",
                            on_release=self.close_pop,
                        ),
                    ],
                )
                self.addbook_popup.auto_dismiss = False
                self.addbook_popup.open()
