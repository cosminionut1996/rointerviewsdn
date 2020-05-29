import unittest
from data_structures.datacenter import Datacenter
import json

class DatacenterDataTest(unittest.TestCase):

    def setUp(self):
        with open('response.json') as fin:
            data = json.load(fin)
        self.dc = Datacenter('Berlin', data['Berlin'] )

    def test_datacenter_init(self):
        self.assertEqual(self.dc.name, "Berlin")
        for cluster in self.dc.clusters:
            if cluster.name == 'BER-1':
                self.assertEqual(cluster.security_level, 1)

    def test_remove_invalid_clusters(self):
        self.assertEqual(len(self.dc.clusters), 4)
        self.dc.remove_invalid_clusters()
        self.assertEqual(len(self.dc.clusters), 2)

if __name__ == '__main__':
    unittest.main()
