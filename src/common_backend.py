"""
Common methods and functions for kivy and qt.
"""

import queues
from bmconfigparser import BMConfigParser


class AddressGenerator:

    @staticmethod
    def start_address_generation(
        entered_label, streamNumberForAddress=1, eighteenByteRipe=False,
        nonceTrialsPerByte=1000, payloadLengthExtraBytes=1000
    ):
        """"Return True if the label is unique"""
        labels = [BMConfigParser().get(obj, 'label')
                  for obj in BMConfigParser().addresses()]
        if entered_label and entered_label not in labels:
            queues.addressGeneratorQueue.put((
                'createRandomAddress', 4, streamNumberForAddress, entered_label, 1,
                "", eighteenByteRipe, nonceTrialsPerByte,
                payloadLengthExtraBytes))
            return True
        return False

    @staticmethod
    def address_validation(instance, entered_label):
        """Checking address validation while creating"""
        labels = [BMConfigParser().get(obj, 'label')
            for obj in BMConfigParser().addresses()]
        if entered_label in labels:
            instance.error = True
            instance.helper_text = 'it is already exist you'\
                ' can try this Ex. ( {0}_1, {0}_2 )'.format(
                    entered_label)
        elif entered_label:
            instance.error = False
        else:
            instance.error = False
            instance.helper_text = 'This field is required'
