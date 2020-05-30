import json
import unittest

from _base_test_case_response_load import BaseTestCaseResponseLoad


class NetworkCollectionTest(BaseTestCaseResponseLoad):

    def setUp(self):
        super().setUp()
        self.nc = self.dc.clusters[0].networks[0]

    def test_invalid_records(self):
        """ Tests that the removal of invalid records is successful. """
        self.assertEqual(len(self.nc.entries), 10)
        self.nc.remove_invalid_records()
        self.assertEqual(len(self.nc.entries), 6)


if __name__ == '__main__':
    unittest.main()
