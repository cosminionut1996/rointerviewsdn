import datetime
from functools import total_ordering

@total_ordering
class Entry:
    def __init__(self, address, available, last_used):
        """
        Constructor for Entry data structure.

        self.address -> str
        self.available -> bool
        self.last_used -> datetime
        """
        self.address = address
        self.available = available
        self.last_used = datetime.datetime.strptime(last_used, r"%d/%m/%y %H:%M:%S")

    def __repr__(self):
        return "[{} | {} | {}]".format(
            self.address,
            self.available,
            self.last_used
        )

    @classmethod
    def _addr_decimal(cls, address):
        address = address.replace('.', '')
        if not address.isdigit():
            return -1
        else:
            return int(address.lstrip('0'))

    def __lt__(self, other):
        return self._addr_decimal(self.address) < self._addr_decimal(other.address)

    def __eq__(self, other):
        return self._addr_decimal(self.address) == self._addr_decimal(other.address)
