import queues
from bmconfigparser import BMConfigParser
from bitmessagekivy.baseclass.common import toast


class AddressGenerator:

    @staticmethod
    def generate_address(entered_label):
        """"Return True if the label is uniqe"""
        streamNumberForAddress = 1
        eighteenByteRipe = False
        nonceTrialsPerByte = 1000
        payloadLengthExtraBytes = 1000
        labels = [BMConfigParser().get(obj, 'label')
                  for obj in BMConfigParser().addresses()]
        if entered_label and entered_label not in labels:
            toast('Address Creating...')
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
