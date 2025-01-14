from .telenium_process import TeleniumTestProcess
from .common import skip_screen_checks
from .common import ordered

test_address = {'receiver': 'BM-2cWmjntZ47WKEUtocrdvs19y5CivpKoi1h'}


class SendMessage(TeleniumTestProcess):
    """Sent Screen Functionality Testing"""
    test_subject = 'Test Subject'
    test_body = 'Hello, \n Hope your are doing good.\n\t This is test message body'

    @skip_screen_checks
    @ordered
    def test_validate_empty_form(self):
        """
            Sending Message From Inbox Screen
            opens a pop-up(screen) which send message from sender to reciever
        """
        # Checking current Screen(Login screen)
        self.assert_wait_no_except('//ScreenManager[@current]', timeout=10, value='login')
        # Click on Composer Icon(Plus icon)
        self.cli.wait_click('//ComposerButton[0]/MDFloatingActionButton[@icon=\"plus\"]', timeout=2)
        # Checking Message Composer Screen(Create)
        self.assertExists("//ScreenManager[@current=\"create\"]", timeout=4)
        # Checking State of Sender's Address Input Field (should be Empty)
        self.assertExists('//DropDownWidget/ScrollView[0]//MDTextField[@text=\"\"]', timeout=3)
        # Checking State of Receiver's Address Input Field (should be Empty)
        self.assertExists('//DropDownWidget/ScrollView[0]//MyTextInput[@text=\"\"]', timeout=2)
        # Checking State of Subject Input Field (shoudl be Empty)
        self.assertExists('//DropDownWidget/ScrollView[0]//MyMDTextField[@text=\"\"]', timeout=2)
        # Click on Send Icon to check validation working
        self.cli.wait_click('//MDActionTopAppBarButton[@icon=\"send\"]', timeout=2)
        # Checking validation Pop up is Opened
        self.assertExists('//MDDialog', timeout=5)
        # Click "OK" button to dismiss the Popup
        self.cli.wait_click('//MDFlatButton[@text=\"Ok\"]', timeout=5)
        # Checking current screen after dialog dismiss
        self.assertExists("//ScreenManager[@current=\"create\"]", timeout=10)

    @skip_screen_checks
    @ordered
    def test_validate_half_filled_form(self):
        """
            Validate the half filled form and press back button to save message in draft box.
        """
        # Checking current screen
        self.assertExists("//ScreenManager[@current=\"create\"]", timeout=2)
        # ADD SENDER'S ADDRESS
        # Checking State of Sender's Address Input Field (Empty)
        self.assertExists('//DropDownWidget/ScrollView[0]//MDTextField[@text=\"\"]', timeout=2)
        # Assert to check Sender's address dropdown closed
        is_open = self.cli.getattr('//Create//CustomSpinner[@is_open]', 'is_open')
        self.assertEqual(is_open, False)
        # Open Sender's Address DropDown
        self.cli.wait_click('//Create//CustomSpinner[0]/ArrowImg[0]', timeout=5)
        # Checking the Address Dropdown is in open State
        is_open = self.cli.getattr('//Create//CustomSpinner[@is_open]', 'is_open')
        # Select Sender's Address from Dropdown
        self.cli.wait_click('//ComposerSpinnerOption[0]', timeout=3)
        # Assert to check Sender's address dropdown closed
        is_open = self.cli.getattr('//Create//CustomSpinner[@is_open]', 'is_open')
        self.assertEqual(is_open, False)
        # Assert check for empty Subject Field
        self.assertNotEqual('//DropDownWidget/ScrollView[0]//MDTextField[0]', '')
        # ADD SUBJECT
        self.cli.setattr('//DropDownWidget/ScrollView[0]//MyMDTextField[0]', 'text', self.test_subject)
        # Checking Subject Field is Entered
        self.assertNotEqual('//DropDownWidget/ScrollView[0]//MyMDTextField[text]', '')
        # Checking BODY Field(EMPTY)
        self.assertExists('//DropDownWidget/ScrollView[0]//ScrollView[0]/MDTextField[@text=\"\"]', timeout=2)
        # ADD BODY
        self.cli.setattr(
            '//DropDownWidget/ScrollView[0]/BoxLayout[0]/ScrollView[0]/MDTextField[0]', 'text', self.test_body)
        # Checking BODY is Entered
        self.assertNotEqual('//DropDownWidget/ScrollView[0]/BoxLayout[0]/ScrollView[0]/MDTextField[text]', '')
        # click on send icon
        self.cli.wait_click('//MDActionTopAppBarButton[@icon=\"send\"]', timeout=2)
        # Checking validation Pop up is Opened
        self.assertExists('//MDDialog', timeout=5)
        # clicked on 'Ok' button to close popup
        self.cli.wait_click('//MDFlatButton[@text=\"Ok\"]', timeout=5)
        # Checking current screen after dialog dismiss
        self.assertExists("//ScreenManager[@current=\"create\"]", timeout=5)

    @skip_screen_checks
    @ordered
    def test_sending_msg_fully_filled_form(self):
        """
            Sending message when all fields are filled
        """
        # ADD RECEIVER ADDRESS
        # Checking Receiver Address Field
        self.assertExists('//DropDownWidget/ScrollView[0]//MyTextInput[@text=\"\"]', timeout=2)
        # Entering Receiver Address
        self.cli.setattr('//DropDownWidget/ScrollView[0]//MyTextInput[0]', "text", test_address['receiver'])
        # Checking Receiver Address filled or not
        self.assertNotEqual('//DropDownWidget/ScrollView[0]//MyTextInput[text]', '')
        # Clicking on send icon
        self.cli.wait_click('//MDActionTopAppBarButton[@icon=\"send\"]', timeout=5)
        # Checking the current screen
        self.assertExists("//ScreenManager[@current=\"inbox\"]", timeout=10)

    @skip_screen_checks
    @ordered
    def test_sent_box(self):
        """
            Checking Message in Sent Screen after sending a Message.
        """
        # this is for opening Nav drawer
        self.cli.wait_click('//MDActionTopAppBarButton[@icon=\"menu\"]', timeout=5)
        # checking state of Nav drawer
        self.assertExists("//MDNavigationDrawer[@state~=\"open\"]", timeout=5)
        # Clicking on Sent Tab
        self.cli.wait_click('//NavigationItem[@text=\"Sent\"]', timeout=5)
        # Checking current screen; Sent
        self.assertExists("//ScreenManager[@current=\"sent\"]", timeout=5)
        # Checking number of Sent messages
        total_sent_msgs = len(self.cli.select("//SwipeToDeleteItem"))
        self.assertEqual(total_sent_msgs, 3)
