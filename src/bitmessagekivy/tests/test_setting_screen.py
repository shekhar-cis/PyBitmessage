from .telenium_process import TeleniumTestProcess


class SettingScreen(TeleniumTestProcess):
    """Setting Screen Functionality Testing"""

    def test_setting_screen(self):
        """Show Setting Screen"""
        # self.cli.sleep(8)
        self.assertCheck_app_launch('//ScreenManager[@current]', timeout=5)
        # print(self.assertTrue('//ScreenManager[@current]', 'inbox'), "self.assertTrue('//ScreenManager[@current]', 'inbox')self.assertTrue('//ScreenManager[@current]', 'inbox')self.assertTrue('//ScreenManager[@current]', 'inbox')self.assertTrue('//ScreenManager[@current]', 'inbox')")
        # self.assertTrue('//ScreenManager[@current]', 'inbox')
        # self.assertCheck_app_launch('//ScreenManager[@current=\"inbox\"]', timeout=5)
        # this is for opening Nav drawer
        self.cli.wait_click('//MDActionTopAppBarButton[@icon=\"menu\"]', timeout=2)
        # checking state of Nav drawer
        self.assertExists("//MDNavigationDrawer[@state~=\"open\"]", timeout=2)
        # this is for scrolling Nav drawer
        self.drag("//NavigationItem[@text=\"Sent\"]", "//NavigationItem[@text=\"Inbox\"]")
        # assert for checking scroll function
        self.assertCheckScrollDown('//ContentNavigationDrawer//ScrollView[0]', timeout=5)
        # this is for opening setting screen
        self.cli.wait_click('//NavigationItem[@text=\"Settings\"]', timeout=3)
        # Checking current screen
        self.assertExists("//ScreenManager[@current=\"set\"]", timeout=2)
