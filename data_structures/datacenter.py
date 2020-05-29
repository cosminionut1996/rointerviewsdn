from .cluster import Cluster

class Datacenter:
    def __init__(self, name, cluster_dict):
        """
        Constructor for Datacenter data structure.

        self.name -> str
        self.clusters -> list(Cluster)
        """
        self.name = name
        self.clusters = [
            Cluster(
                network_name,
                network_details['networks'],
                network_details['security_level']
            )
            for network_name, network_details in cluster_dict.items()
        ]

    def remove_invalid_clusters(self):
        """
        Removes invalid objects from the clusters list.
        """

        pass
