# pylint: disable=too-many-instance-attributes, too-few-public-methods

"""
Kivy State variables are assigned here, they are separated from state.py
=================================
"""


class KivyStateVariables(object):
    """This Class hold all the kivy state variables"""

    def __init__(self):
        self.association = ''
        self.navinstance = None
        self.mail_id = 0
        self.my_address_obj = None
        self.detail_page_type = None
        self.ackdata = None
        self.status = None
        self.screen_density = None
        self.msg_counter_objs = None
        self.check_sent_acc = None
        self.sent_count = 0
        self.inbox_count = 0
        self.trash_count = 0
        self.draft_count = 0
        self.all_count = 0
        self.searching_text = ''
        self.search_screen = ''
        self.send_draft_mail = None
        self.is_allmail = False
        self.in_composer = False
        self.available_credit = 0
        self.in_sent_method = False
        self.in_search_mode = False
        self.image_dir = None


association = ''
navinstance = None
mail_id = 0
my_address_obj = None
detail_page_type = None
ackdata = None
status = None
screen_density = None
msg_counter_objs = None
check_sent_acc = None
sent_count = 0
inbox_count = 0
trash_count = 0
draft_count = 0
all_count = 0
searching_text = ''
search_screen = ''
send_draft_mail = None
is_allmail = False
in_composer = False
available_credit = 0
in_sent_method = False
in_search_mode = False
image_dir = None
