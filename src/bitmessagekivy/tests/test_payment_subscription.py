from time import time
from .telenium_process import TeleniumTestProcess


class PaymentScreen(TeleniumTestProcess):
    """SubscriptionPayment Screen Functionality Testing"""

    def test_select_subscripton(self):
        """Select Subscripton From List of Subscriptons"""
        print("=====================Test -Select Subscripton From List of Subscriptons=====================")
        self.cli.sleep(10)
        # this is for opening Nav drawer
        self.cli.wait_click('//MDActionTopAppBarButton[@icon=\"menu\"]', timeout=3)
        # checking state of Nav drawer
        self.assertExists("//MDNavigationDrawer[@state~=\"open\"]", timeout=2)
        # Dragging from sent to inbox to get Payment tab.
        self.drag("//NavigationItem[@text=\"Sent\"]", "//NavigationItem[@text=\"Inbox\"]")
        # assert for checking scroll function
        self.assertCheckScrollDown('//ContentNavigationDrawer//ScrollView[0]', timeout=3)
        self.assertExists('//NavigationItem[@text=\"Purchase\"]', timeout=3)
        # this is for opening Payment screen
        self.click_on('//NavigationItem[@text=\"Purchase\"]', seconds=2)
        # Assert for checking Current Screen
        self.assertExists("//Payment[@name~=\"payment\"]", timeout=4)
        self.drag(
            '//ProductCategoryLayout[0]/ProductLayout[1]',
            '//ProductCategoryLayout[0]/ProductLayout[0]')
        # assert for checking scroll function
        self.assertExists('//MDRaisedButton[3]', timeout=3)
        self.cli.wait_click('//MDRaisedButton[@text=\"BUY\"]', timeout=2)
        self.click_on('//ScrollView[0]/ListItemWithLabel[0]', seconds=1)
        self.click_on('//MDRaisedButton[3]', seconds=1)
        self.assertExists("//Payment[@name~=\"payment\"]", timeout=2)
        