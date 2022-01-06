# pylint: disable=too-many-lines,import-error,no-name-in-module,unused-argument, no-else-return,  unused-variable
# pylint: disable=too-many-ancestors,too-many-locals,useless-super-delegation, attribute-defined-outside-init
# pylint: disable=protected-access, super-with-arguments, pointless-statement
# pylint: disable=import-outside-toplevel,ungrouped-imports,wrong-import-order,unused-import,arguments-differ
# pylint: disable=invalid-name,unnecessary-comprehension,broad-except,simplifiable-if-expression,no-member
# pylint: disable=too-many-return-statements, unnecessary-pass

"""
QR Code Generator
"""

from pybitmessage import state
from pybitmessage.baseclass.common import toast
from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from kivy_garden.qrcode import QRCodeWidget


class ShowQRCode(Screen):
    """ShowQRCode Screen class for kivy Ui"""
    address = StringProperty()

    def qrdisplay(self, instasnce, address):
        """Method used for showing QR Code"""
        self.ids.qr.clear_widgets()
        state.kivyapp.set_toolbar_for_QrCode()
        self.address = address
        self.ids.qr.add_widget(QRCodeWidget(data=address))
        self.ids.qr.children[0].show_border = False
        instasnce.parent.parent.parent.dismiss()
        toast('Show QR code')
