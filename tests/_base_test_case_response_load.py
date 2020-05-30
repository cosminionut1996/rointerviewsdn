import json
import unittest

from data_structures.datacenter import Datacenter


class BaseTestCaseResponseLoad(unittest.TestCase):

    def setUp(self):
        with open('response.json') as fin:
            data = json.load(fin)
        self.dc = Datacenter('Berlin', data['Berlin'] )
