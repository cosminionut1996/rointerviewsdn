from .entry import Entry
import ipaddress

class NetworkCollection:
    def __init__(self, ipv4_network, raw_entry_list):
        """
        Constructor for NetworkCollection data structure.

        self.ipv4_network -> ipaddress.IPv4Network
        self.entries -> list(Entry)
        """
        self.ipv4_network = ipaddress.ip_network(ipv4_network)
        self.entries = [
            Entry(
                entry['address'],
                entry['available'],
                entry['last_used']
            ) for entry in raw_entry_list
        ]

    def remove_invalid_records(self):
        """
        Removes invalid objects from the entries list.
        """
        _entries = self.entries
        for entry in self.entries:
            valid = True
            try:
                addr = ipaddress.ip_address(entry.address)
            except ValueError:
                valid = False
            else:
                if addr not in self.ipv4_network:
                    valid = False

            if not valid:
                _entries.remove(entry)
        self.entries = _entries

    def sort_records(self):
        """
        Sorts the list of associated entries in ascending order.
        DO NOT change this method, make the changes in entry.py :)
        """

        self.entries = sorted(self.entries)
