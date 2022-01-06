# pylint: disable=too-many-lines,import-error,no-name-in-module,unused-argument, no-else-return,  unused-variable
# pylint: disable=too-many-ancestors,too-many-locals,useless-super-delegation, attribute-defined-outside-init
# pylint: disable=protected-access, super-with-arguments
# pylint: disable=import-outside-toplevel,ungrouped-imports,wrong-import-order,unused-import,arguments-differ
# pylint: disable=invalid-name,unnecessary-comprehension,broad-except,simplifiable-if-expression,no-member
# pylint: disable=too-many-return-statements, unnecessary-pass

"""
Network Screen
"""

from kivy.clock import Clock
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen


class NetworkStat(Screen):
    """NetworkStat class for kivy Ui"""

    text_variable_1 = StringProperty(
        '{0}::{1}'.format('Total Connections', '0'))
    text_variable_2 = StringProperty(
        'Processed {0} per-to-per messages'.format('0'))
    text_variable_3 = StringProperty(
        'Processed {0} brodcast messages'.format('0'))
    text_variable_4 = StringProperty(
        'Processed {0} public keys'.format('0'))
    text_variable_5 = StringProperty(
        'Processed {0} object to be synced'.format('0'))

    def __init__(self, *args, **kwargs):
        """Init method for network stat"""
        super(NetworkStat, self).__init__(*args, **kwargs)
        Clock.schedule_interval(self.init_ui, 1)

    def init_ui(self, dt=0):
        """Clock Schdule for method networkstat screen"""
        pass
