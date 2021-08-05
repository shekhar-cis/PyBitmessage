from .telenium_process import TeleniumTestProcess


class TrashMessage(TeleniumTestProcess):
    """Trash Screen Functionality Testing"""

    def test_delete_trash_message(self):
        """Delete Trash message permanently from trash message listing"""
        try:
            # checking current screen
            self.assertExists("//ScreenManager[@current=\"inbox\"]", timeout=5)
        except:
            self.cli.sleep(8)
            # checking current screen
            self.assertExists("//ScreenManager[@current=\"inbox\"]", timeout=5)
        # this is for opening Nav drawer
        self.cli.wait_click('//MDActionTopAppBarButton[@icon=\"menu\"]', timeout=5)
        # checking state of Nav drawer
        self.assertExists("//MDNavigationDrawer[@state~=\"open\"]", timeout=5)
        # this is for opening Trash screen
        self.click_on('//NavigationItem[@text=\"Trash\"]', seconds=2)
        # checking current screen(Trash Screen)
        self.assertExists("//ScreenManager[@current=\"trash\"]", timeout=3)
        # Checking Trash Icon is in disable state
        self.assertTrue('//MDList[0]/CustomSwipeToDeleteItem[0]//MDIconButton[@disabled]', 'True')
        # This is for swiping message to activate delete icon.
        self.drag(
            '//Trash[0]//TwoLineAvatarIconListItem[0]/BoxLayout[1]',
            '//Trash[0]//TwoLineAvatarIconListItem[0]/BoxLayout[2]')
        # Assert to check the drag is worked (Trash icon Activated)
        self.assertTrue('//MDList[0]/CustomSwipeToDeleteItem[0]//MDIconButton[@disabled]', 'False')
        # Checking the Trash Icon after swipe.
        self.assertExists("//MDList[0]/CustomSwipeToDeleteItem[0]//MDIconButton[@icon~=\"trash-can\"]", timeout=2)
        # Clicking on Trash icon to open Confirm delete pop up
        self.click_on('//MDList[0]/CustomSwipeToDeleteItem[0]', seconds=1)
        # Checking Confirm delete Popup is Opened
        self.assertTrue('//MDList[0]/CustomSwipeToDeleteItem[@_opens_process]', 'True')
        # clicking on Trash Box icon to delete message.
        self.cli.wait_click('//MDList[0]/CustomSwipeToDeleteItem[0]//MDIconButton[0]', timeout=2)
        # Checking the popup screen is closed.
        self.assertTrue('//MDList[0]/CustomSwipeToDeleteItem[@_opens_process]', 'False')
        # Clicking on 'Yes' Button on Popup to confirm delete.
        self.click_on('//MDFlatButton[@text=\"Yes\"]', seconds=1.1)
        # checking current screen(Trash Screen)
        self.assertExists("//ScreenManager[@current=\"trash\"]", timeout=2)
        total_trash_msgs = len(self.cli.select("//CustomSwipeToDeleteItem"))
        # Checking messages count after delete.
        self.assertEqual(total_trash_msgs, 1)
