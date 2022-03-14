import state

from bitmessagekivy.get_platform import platform

from kivymd.uix.button import MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel

from bitmessagekivy.baseclass.popup import AddbookDetailPopup
# from bitmessagekivy.baseclass.addressbook import AddressBook

class HelperAddressBook:
    """Widget used in Addressbook are here"""

    @staticmethod
    def default_label_when_empty():
            content = MDLabel(
                font_style='Caption',
                theme_text_color='Primary',
                text="No contact found!" if state.searcing_text
                else "No contact found yet...... ",
                halign='center',
                size_hint_y=None,
                valign='top')
            return content

    # @staticmethod
    # def address_detail_popup(address, label, instance, **args):
    #             obj = AddbookDetailPopup()
    #             address_label = obj.address_label = label
    #             address = obj.address = address
    #             width = .9 if platform == 'android' else .8
    #             addbook_popup = MDDialog(
    #                 type="custom",
    #                 size_hint=(width, .25),
    #                 content_cls=obj,
    #                 buttons=[
    #                     MDRaisedButton(
    #                         text="Send message to",
    #                         on_release=AddressBook.send_message_to,
    #                     ),
    #                     MDRaisedButton(
    #                         text="Save",
    #                         on_release=AddressBook.update_addbook_label,
    #                     ),
    #                     MDRaisedButton(
    #                         text="Cancel",
    #                         on_release=AddressBook.close_pop,
    #                     ),
    #                 ],
    #             )
    #             addbook_popup.auto_dismiss = False
    #             addbook_popup.open()
