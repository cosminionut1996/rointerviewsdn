import datetime

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
        return "{} | {} | {}".format(
            self.address,
            self.available,
            self.last_used
        )
