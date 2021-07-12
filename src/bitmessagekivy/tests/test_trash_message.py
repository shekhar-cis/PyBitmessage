from datetime import datetime
from os import wait
from socket import timeout
from time import sleep

from telenium.mods.telenium_client import selectFirst, kivythread, TeleniumMotionEvent, nextid, telenium_input, run_telenium

from .telenium_process import TeleniumTestProcess


class TrashMessage(TeleniumTestProcess):
    
    def smart_click(self, click_on, sleep):
        click_on = self.cli.click_on(click_on)
        sleep = self.cli.sleep(sleep)
        
    """Trash Screen Functionality Testing"""

    def test_delete_trash_message(self):
        """Delete Trash message permanently from trash message listing"""
        self.cli.sleep(12)
        self.smart_click('//MDToolbar/BoxLayout[0]/MDActionTopAppBarButton[0]', 3)
        self.smart_click('//NavigationItem[4]', 3)
        self.assertExists("//Trash[@name~=\"trash\"]", timeout=2)
        self.cli.drag(
            '//MDList[0]/CutsomSwipeToDeleteItem[0]//TwoLineAvatarIconListItem[0]/BoxLayout[1]',
            '//MDList[0]/CutsomSwipeToDeleteItem[0]//TwoLineAvatarIconListItem[0]/BoxLayout[2]',1)
        self.cli.sleep(5)
        self.smart_click('//MDList[0]/CutsomSwipeToDeleteItem[0]', 3)
        self.smart_click('//MDList[0]/CutsomSwipeToDeleteItem[0]//MDIconButton[0]', 3)
        self.smart_click('//MDDialog/MDCard[0]/AnchorLayout[0]/MDBoxLayout[0]/MDFlatButton[0]', 3)
        self.smart_click('//MDDialog/DialogFakeCard[0]/AnchorLayout[0]/MDBoxLayout[0]/MDFlatButton[0]', 3)
        total_trash_msgs = len(self.cli.select("//CutsomSwipeToDeleteItem"))
        self.assertEqual(total_trash_msgs, 1)
