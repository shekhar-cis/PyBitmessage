from datetime import datetime
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.metrics import dp
from kivymd.uix.list import (
    ILeftBody,
    IRightBodyTouch,
)
from kivy.uix.image import Image
from kivymd.uix.label import MDLabel
from bitmessagekivy.get_platform import platform
from kivymd.toast import kivytoast
from kivymd.uix.card import MDCardSwipe
from kivymd.uix.chip import MDChip
from kivy.properties import (
    NumericProperty,
    StringProperty
)
from kivymd.uix.label import MDLabel

import state

ThemeClsColor = [0.12, 0.58, 0.95, 1]


data_screens = {
    "MailDetail": {
        "kv_string": "maildetail",
        "Factory": "MailDetail()",
        "name_screen": "mailDetail",
        "object": 0,
        "Import": "from bitmessagekivy.baseclass.maildetail import MailDetail",
    },
}


def chipTag(text):
    """This method is used for showing chip tag"""
    obj = MDChip()
    # obj.size_hint = (None, None)
    obj.size_hint = (0.16 if platform == "android" else 0.08, None)
    obj.text = text
    obj.icon = ""
    obj.pos_hint = {
        "center_x": 0.91 if platform == "android" else 0.94,
        "center_y": 0.3
    }
    obj.height = dp(18)
    obj.text_color = (1, 1, 1, 1)
    obj.radius = [8]
    return obj


# def initailize_detail_page(manager):
#     if not manager.has_screen(
#         data_screens['MailDetail']["name_screen"]
#     ):
#         Builder.load_file(
#             os.path.join(
#                 # os.environ["KITCHEN_SINK_ROOT"],
#                 os.path.dirname(os.path.dirname(__file__)),
#                 "kv",
#                 "maildetail.kv",
#             )
#         )
#         if "Import" in data_screens['MailDetail']:
#             exec(data_screens['MailDetail']["Import"])
#         screen_object = eval(data_screens['MailDetail']["Factory"])
#         data_screens['MailDetail']["object"] = screen_object
#         manager.add_widget(screen_object)
#     manager.current = data_screens['MailDetail']["name_screen"]


def toast(text):
    """Function will display the toast message"""
    kivytoast.toast(text)

def showLimitedCnt(total_msg):
    """This method set the total count limit in badge_text"""
    return "99+" if total_msg > 99 else str(total_msg)


def avatarImageFirstLetter(letter_string):
    """This function is used to the first letter for the avatar image"""
    try:
        if isinstance(letter_string, int):
            return letter_string[0]
        elif isinstance(letter_string, str) and letter_string[0].isalnum():
            return letter_string.title()[0]
        else:
            return '!'
    except IndexError:
        return '!'

def AddTimeWidget(time):  # pylint: disable=redefined-outer-name, W0201
    """This method is used to create TimeWidget"""
    action_time = TimeTagRightSampleWidget(
        text=str(ShowTimeHistoy(time)),
        font_style="Caption",
        size=[120, 140] if platform == "android" else [64, 80],
    )
    action_time.font_size = "11sp"
    return action_time


def ShowTimeHistoy(act_time):
    """This method is used to return the message sent or receive time"""
    action_time = datetime.fromtimestamp(int(act_time))
    crnt_date = datetime.now()
    duration = crnt_date - action_time
    display_data = (
        action_time.strftime("%d/%m/%Y")
        if duration.days >= 365
        else action_time.strftime("%I:%M %p").lstrip("0")
        if duration.days == 0 and crnt_date.strftime("%d/%m/%Y") == action_time.strftime("%d/%m/%Y")
        else action_time.strftime("%d %b")
    )
    return display_data


# pylint: disable=too-few-public-methods
class AvatarSampleWidget(ILeftBody, Image):
    """AvatarSampleWidget class for kivy Ui"""


class TimeTagRightSampleWidget(IRightBodyTouch, MDLabel):
    """TimeTagRightSampleWidget class for Ui"""


class SwipeToDeleteItem(MDCardSwipe):
    """Swipe delete class for App UI"""
    text = StringProperty()
    cla = Window.size[0] / 2
    # cla = 800
    swipe_distance = NumericProperty(cla)
    opening_time = NumericProperty(0.5)


class CutsomSwipeToDeleteItem(MDCardSwipe):
    """Custom swipe delete class for App UI"""
    text = StringProperty()
    cla = Window.size[0] / 2
    swipe_distance = NumericProperty(cla)
    opening_time = NumericProperty(0.5)


def empty_screen_label(label_str=None, no_search_res_found=None):
    """Returns default text on screen when no address is there."""
    content = MDLabel(
        font_style='Caption',
        theme_text_color='Primary',
        text=no_search_res_found if state.searcing_text else label_str,
        halign='center',
        size_hint_y=None,
        valign='top')
    return content


def mdlist_message_content(queryreturn, data, max_len=25, min_len=10):
    for mail in queryreturn:
        third_text = mail[3].replace('\n', ' ')
        data.append({
            'text': mail[1].strip(),
            'secondary_text': mail[2][:10] + '...........' if len(
                mail[2]) > 10 else mail[2] + '\n' + " " + (
                    third_text[:25] + '...!') if len(
                        third_text) > 25 else third_text,
            'ackdata': mail[5], 'senttime': mail[6]})
