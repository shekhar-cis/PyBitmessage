# pylint: disable=too-many-lines,import-error,no-name-in-module,unused-argument, no-else-return,  unused-variable
# pylint: disable=too-many-ancestors,too-many-locals,useless-super-delegation, attribute-defined-outside-init, no-self-use
# pylint: disable=protected-access, super-with-arguments, pointless-statement, no-method-argument, too-many-function-args
# pylint: disable=import-outside-toplevel,ungrouped-imports,wrong-import-order,unused-import,arguments-differ, too-few-public-methods
# pylint: disable=invalid-name,unnecessary-comprehension,broad-except,simplifiable-if-expression,no-member, consider-using-in
# pylint: disable=too-many-return-statements, unnecessary-pass, bad-option-value, abstract-method, consider-using-f-string

'''
    This is for payment related part
'''

from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.behaviors.elevation import RectangularElevationBehavior
from kivy.uix.screenmanager import Screen

from kivymd.uix.label import MDLabel
from kivymd.uix.list import (
    IRightBodyTouch,
    OneLineAvatarIconListItem
)


class Payment(Screen):
    """Payment Screen class for kivy Ui"""

    @staticmethod
    def create_hidden_payment_address():
        """This is basically used for creating hidden address used in payment for purchasing credits"""
        pass


class Category(BoxLayout, RectangularElevationBehavior):
    """Category class for kivy Ui"""
    elevation_normal = .01


class ProductLayout(BoxLayout, RectangularElevationBehavior):
    """ProductLayout class for kivy Ui"""
    elevation_normal = .01


class PaymentMethodLayout(BoxLayout):
    """PaymentMethodLayout class for kivy Ui"""


class ListItemWithLabel(OneLineAvatarIconListItem):
    """ListItemWithLabel class for kivy Ui"""


class RightLabel(IRightBodyTouch, MDLabel):
    """RightLabel class for kivy Ui"""
