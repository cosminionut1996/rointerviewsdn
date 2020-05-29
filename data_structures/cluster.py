from .network_collection import NetworkCollection

class Cluster:
    def __init__(self, name, network_dict, security_level):
        """
        Constructor for Cluster data structure.

        self.name -> str
        self.security_level -> int
        self.networks -> list(NetworkCollection)
        """
        self.name = name
        self.security_level = security_level
        self.networks = [
            NetworkCollection(ipv4_network, entries)
            for ipv4_network, entries in network_dict.items()
        ]
