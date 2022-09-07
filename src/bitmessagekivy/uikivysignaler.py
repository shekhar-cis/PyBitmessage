"""
Ui Singnaler for kivy interface
"""
from threading import Thread
import logging
import queues
import state
from kivy.app import App
from bitmessagekivy.baseclass.common import kivy_state_variables

logger = logging.getLogger('default')


class UIkivySignaler(Thread):
    """Kivy ui signaler"""

    def __init__(self, *args, **kwargs):
        super(UIkivySignaler, self).__init__(*args, **kwargs)
        self.kivy_state = kivy_state_variables()

    def run(self):
        self.kivy_state.sql_ready.wait()
        # kivyuisignaler.acquire()
        while state.shutdown == 0:
            try:
                command, data = queues.UISignalQueue.get()
                if command == 'writeNewAddressToTable':
                    address = data[1]
                    App.get_running_app().identity_list.append(address)
                elif command == 'updateSentItemStatusByAckdata':
                    App.get_running_app().status_dispatching(data)
                elif command == 'writeNewpaymentAddressToTable':
                    pass
            except Exception as e:
                logger.debug(e)
