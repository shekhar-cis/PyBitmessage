"""
The objectProcessor thread, of which there is only one,
processes the network objects
"""
import logging
import random
import threading

from pybitmessage import state

logger = logging.getLogger('default')


class objectProcessor(threading.Thread):
    """
    The objectProcessor thread, of which there is only one, receives network
    objects (msg, broadcast, pubkey, getpubkey) from the receiveDataThreads.
    """
    def __init__(self):
        threading.Thread.__init__(self, name="objectProcessor")
        random.seed()
        self.successfullyDecryptMessageTimings = []

    def run(self):
        """Process the objects from `.queues.objectProcessorQueue`"""
        while True:
            # pylint: disable=unused-variable
            if state.shutdown:
                state.shutdown = 2
                break
