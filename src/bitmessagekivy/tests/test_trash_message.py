from time import sleep
from .telenium_process import TeleniumTestProcess


class TrashMessage(TeleniumTestProcess):
    """Trash Screen Functionality Testing"""

    def test_delete_trash_message(self):
        """Delete Trash message permanently from trash message listing"""
        # This is for checking Current screen
        self.assert_wait_no_except('//ScreenManager[@current]', timeout=18, value='inbox')
        # This is for checking the Side nav Bar id closed
        self.assertExists('//MDNavigationDrawer[@status~=\"closed\"]', timeout=5)
        # This is for checking the menu button is appeared
        self.assertExists('//MDActionTopAppBarButton[@icon~=\"menu\"]', timeout=5)
        # this is for opening Nav drawer
        self.cli.wait_click('//MDActionTopAppBarButton[@icon=\"menu\"]', timeout=5)
        # checking state of Nav drawer
        self.assertExists("//MDNavigationDrawer[@state~=\"open\"]", timeout=5)
        # this is for opening Trash screen
        self.cli.wait_click('//NavigationItem[@text=\"Trash\"]', timeout=3)
        # checking current screen(Trash Screen)
        # self.assertExists("//ScreenManager[@current=\"trash\"]", timeout=3)
        self.assert_wait_no_except('//ScreenManager[@current]', timeout=5, value='trash')
        self.cli.sleep(2)
        self.cli.drag(
            '//Trash[0]//TwoLineAvatarIconListItem[0]/BoxLayout[1]',
            '//Trash[0]//TwoLineAvatarIconListItem[0]/BoxLayout[2]', 1)
        # Checking Trash Icon is in disable state
        # self.assertTrue('//MDList[0]/CustomSwipeToDeleteItem[0]//MDIconButton[@disabled]', False)
        # is_trash_icon = self.cli.getattr('//Trash//MDList[0]/CustomSwipeToDeleteItem[0]/MDCardSwipeLayerBox[0]/MDIconButton[@disabled]', 'disabled')
        # self.assertEqual(is_trash_icon, True)
        # is_drag_open = self.cli.getattr('//Trash//MDList[0]/CustomSwipeToDeleteItem[@_opens_process]', '_opens_process')
        # self.assertEqual(is_drag_open, False)
        # print(is_drag_open, '=s--------------------------------------1')

         # self.cli.sleep(3)
        # self.cli.wait_click('//Trash[0]//TwoLineAvatarIconListItem[0]/BoxLayout[1]', timeout=5)
        # This is for swiping message to activate delete icon.

        # self.swipe_drag(is_trash_icon, timeout=5)
        # self.swipe_drag(is_drag_open, timeout=5)
        # self.cli.sleep(1)
        # self.cli.wait_click('//MDList[0]/CustomSwipeToDeleteItem[0]/MDCardSwipeLayerBox[0]', timeout=2)

        # self.cli.drag(
        #     '//Trash[0]//TwoLineAvatarIconListItem[0]/BoxLayout[1]',
        #     '//Trash[0]//TwoLineAvatarIconListItem[0]/BoxLayout[2]', 1)
        # self.cli.wait_click('//MDList[0]/CustomSwipeToDeleteItem[0]/MDCardSwipeLayerBox[0]', timeout=2)

        # is_drag_open = self.cli.getattr('//Trash//MDList[0]/CustomSwipeToDeleteItem[@_opens_process]', '_opens_process')
        # self.assertEqual(is_drag_open, False)
        # print(is_drag_open, '--------------------------------------2')

        # Assert to check the drag is worked (Trash icon Activated)
        # self.assertExists("//MDList[0]/CustomSwipeToDeleteItem[0]//MDIconButton[@icon~=\"trash-can\"]", timeout=2)
        # self.cli.wait_click('//MDList[0]/CustomSwipeToDeleteItem[0]/MDCardSwipeLayerBox[0]')
        # self.assertEqual(is_trash_icon, False)
        # self.assertEqual(is_trash_icon, False)
        # Checking the Trash Icon after swipe.

        # Clicking on Trash icon to open Confirm delete pop up
        # self.cli.wait_click('//MDList[0]/Cust omSwipeToDeleteItem[0]', timeout=3)
        # checking current screen(Trash Screen)
        # self.cli.sleep(3)
        # self.cli.wait_click('//NavigationItem[@text=\"Trash\"]', timeout=3)
        # self.cli.sleep(3)
        
        # Checking Confirm delete Popup is Opened
        # self.assertTrue('//MDList[0]/CustomSwipeToDeleteItem[@_opens_process]', True)

        # clicking on Trash Box icon to delete message.
        # self.cli.click_on('//MDList[0]/CustomSwipeToDeleteItem[0]//MDIconButton[@icon=\"trash-can\"]')
        # self.assertEqual(is_drag_open, True)
        sleep(5)

        self.cli.click_on('//Trash//MDList[0]/CustomSwipeToDeleteItem[0]//MDIconButton[@icon=\"trash-can\"]')
        print(self.cli.getattr('//Trash//MDList[0]/CustomSwipeToDeleteItem[0]//MDIconButton[@icon]', 'icon'), '=====================icon')
        # self.assert_wait_no_except('//ScreenManager[@current]', timeout=6, value='trash')
        sleep(5)
        # Checking the popup screen is closed.
        # self.cli.wait_click('//MDList[0]/CustomSwipeToDeleteItem[0]//MDIconButton[@icon=\"trash-can\"]', timeout=5)
        # is_drag_open = self.cli.getattr('//Trash//MDList[0]/CustomSwipeToDeleteItem[@_opens_process]', '_opens_process')
        # self.assertEqual(is_drag_open, False)
        # print(is_drag_open, '--------------------------------------3')


        # self.assertTrue('//MDList[0]/CustomSwipeToDeleteItem[@_opens_process]', True)
        self.assert_wait_no_except('//ScreenManager[@current]', timeout=15, value='trash')
        is_trash_icon = self.cli.getattr('//Trash//MDList[0]/CustomSwipeToDeleteItem[0]/MDCardSwipeLayerBox[0]/MDIconButton[@disabled]', 'disabled')
        # self.cli.sleep(10)
        is_trash_icon = self.cli.getattr('//Trash//MDList[0]/CustomSwipeToDeleteItem[0]/MDCardSwipeLayerBox[0]/MDIconButton[@disabled]', 'disabled')
        # self.cli.wait_click('//MDList[0]/CustomSwipeToDeleteItem[0]//MDIconButton[@icon=\"trash-can\"]', timeout=5)
        is_drag_open = self.cli.getattr('//Trash//MDList[0]/CustomSwipeToDeleteItem[@_opens_process]', '_opens_process')
        # self.assertEqual(is_drag_open, False)
        # print(is_drag_open, '--------------------------------------4')

        # Clicking on 'Yes' Button on Popup to confirm delete.
        # self.cli.wait_click('//MDFlatButton[@text=\"Yes\"]', timeout=5)
        # checking current screen(Trash Screen)
        total_trash_msgs = len(self.cli.select("//CustomSwipeToDeleteItem"))
        # Checking messages count after delete.
        self.assertEqual(total_trash_msgs, 1)
