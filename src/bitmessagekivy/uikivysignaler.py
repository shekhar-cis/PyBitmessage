"""
Ui Singnaler for kivy interface
"""
from threading import Thread

import queues
import state
from semaphores import kivyuisignaler
from bitmessagekivy.baseclass.common import kivy_state_variables


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
                    state.kivyapp.variable_1.append(address)
                # elif command == 'rerenderAddressBook':
                #     state.kivyapp.obj_1.refreshs()
                # Need to discuss this
                elif command == 'writeNewpaymentAddressToTable':
                    pass
                elif command == 'updateSentItemStatusByAckdata':
                    state.kivyapp.status_dispatching(data)
            except Exception as e:
                print(e)
