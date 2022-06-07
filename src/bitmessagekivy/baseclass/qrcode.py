from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from kivy_garden.qrcode import QRCodeWidget
from bitmessagekivy.baseclass.common import toast
from kivy.app import App


class ShowQRCode(Screen):
    """ShowQRCode Screen class for kivy Ui"""
    address = StringProperty()


    def __init__(self, *args, **kwargs):
        """Instantiate kivy state variable"""
        super(ShowQRCode, self).__init__(*args, **kwargs)
        self.kivy_running_app = App.get_running_app()

    def qrdisplay(self, instasnce, address):
        """Method used for showing QR Code"""
        self.ids.qr.clear_widgets()
        self.kivy_running_app.set_toolbar_for_QrCode()
        self.address = address
        self.ids.qr.add_widget(QRCodeWidget(data=self.address))
        self.ids.qr.children[0].show_border = False
        instasnce.parent.parent.parent.dismiss()
        toast('Show QR code')
