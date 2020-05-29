import unittest
from data_structures.datacenter import Datacenter
import json

class DatacenterDataTest(unittest.TestCase):

    def test_datacenter_init(self):
        with open('response.json') as fin:
            data = json.load(fin)

        dc = Datacenter('Berlin', data['Berlin'] )
        self.assertEqual(dc.name, "Berlin")
        for cluster in dc.clusters:
            if cluster.name == 'BER-1':
                self.assertEqual(cluster.security_level, 1)


if __name__ == '__main__':
    unittest.main()
