"""
Bitmessage mock
"""
from pybitmessage.class_addressGenerator import addressGenerator
from pybitmessage.inventory import Inventory
from pybitmessage.bmconfigparser import BMConfigParser
from pybitmessage import state


class MockMain:
    """Mock main function"""

    def start(self):
        """Start main application"""
        # pylint: disable=too-many-statements,too-many-branches,too-many-locals, unused-variable
        config = BMConfigParser()
        daemon = config.safeGetBoolean('bitmessagesettings', 'daemon')
        # Start the address generation thread
        addressGeneratorThread = addressGenerator()
        # close the main program even if there are threads left
        addressGeneratorThread.daemon = True
        addressGeneratorThread.start()
        Inventory()
        from pybitmessage.mpybit import NavigateApp
        state.kivyapp = NavigateApp()
        state.kivyapp.run()




def main():
    """Triggers main module"""
    mainprogram = MockMain()
    mainprogram.start()


if __name__ == "__main__":
    main()
