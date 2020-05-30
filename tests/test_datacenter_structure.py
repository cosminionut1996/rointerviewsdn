import json
import unittest

from _base_test_case_response_load import BaseTestCaseResponseLoad


class DatacenterDataTest(BaseTestCaseResponseLoad):

    def test_datacenter_init(self):
        """ Tests the datacenter constructor. """
        self.assertEqual(self.dc.name, "Berlin")
        for cluster in self.dc.clusters:
            if cluster.name == 'BER-1':
                self.assertEqual(cluster.security_level, 1)

    def test_remove_invalid_clusters(self):
        """ Tests removal of invalid clusters. """
        self.assertEqual(len(self.dc.clusters), 4)
        self.dc.remove_invalid_clusters()
        self.assertEqual(len(self.dc.clusters), 2)

        for cluster in self.dc.clusters:
            self.assertEqual(
                self.dc.name[:3].upper(),
                cluster.name[:3]
            )
            self.assertEqual(cluster.name[3], '-')
            self.assertTrue(cluster.name[4:].isdigit())

if __name__ == '__main__':
    unittest.main()
