"""The Inventory singleton"""

# TODO make this dynamic, and watch out for frozen, like with messagetypes
import storage.filesystem
import storage.sqlite
from bmconfigparser import BMConfigParser
from singleton import Singleton


@Singleton
class Inventory():
    """
    Inventory singleton class which uses storage backends
    to manage the inventory.
    """
    def __init__(self):
        self._moduleName = BMConfigParser().safeGet("inventory", "storage")
        self._inventoryClass = getattr(
            getattr(storage, self._moduleName),
            "{}Inventory".format(self._moduleName.title())
        )
        self._realInventory = self._inventoryClass()
        self.numberOfInventoryLookupsPerformed = 0

    # cheap inheritance copied from asyncore
    def __getattr__(self, attr):
        # if attr == "__contains__":
        #     self.numberOfInventoryLookupsPerformed += 1
        try:
            realRet = getattr(self._realInventory, attr)
        except AttributeError:
            raise AttributeError(
                "%s instance has no attribute '%s'" %
                (self.__class__.__name__, attr)
            )
        else:
            return realRet

    # on python3 we have separately added __contains__ method
    def __contains__(self, attr):
        self.numberOfInventoryLookupsPerformed += 1
        return getattr(self._realInventory, '__contains__')(attr)

    # on python3 we have separately added __setitem__ method
    def __setitem__(self, hash_, value):
        return getattr(self._realInventory,'__setitem__')(hash_,value)

    # hint for pylint: this is dictionary like object
    def __getitem__(self, key):
        return self._realInventory[key]