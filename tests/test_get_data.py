import json
import unittest

from main import get_data


class GetDataTest(unittest.TestCase):

    def test_get_data(self):
        """ Test that compares the retrieved data with the expected data that's stored locally """
        remote_data = get_data('http://www.mocky.io/v2/5e539b332e00007c002dacbe')
        with open('response.json') as fin:
            local_data = json.load(fin)
        self.assertDictEqual(remote_data, local_data)

    def test_get_data_fail(self):
        """ Tests that a failed call to get data returns a None value. """
        self.assertIsNone(get_data('this_must_fail', 5, 0))


if __name__ == '__main__':
    unittest.main()
