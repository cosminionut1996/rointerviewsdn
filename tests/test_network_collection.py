import unittest
from data_structures.datacenter import Datacenter
import json

class NetworkCollectionTest(unittest.TestCase):

    def setUp(self):
        with open('response.json') as fin:
            data = json.load(fin)

        dc = Datacenter('Berlin', data['Berlin'])
        self.nc = dc.clusters[0].networks[0]

    def test_invalid_records(self):
        self.assertEqual(len(self.nc.entries), 10)
        self.nc.remove_invalid_records()
        self.assertEqual(len(self.nc.entries), 6)


if __name__ == '__main__':
    unittest.main()
