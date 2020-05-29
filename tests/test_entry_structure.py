import unittest
from data_structures.entry import Entry


class EntryStructureTest(unittest.TestCase):

    def test_entry_ordering(self):
        e1 = Entry("192.168.2.1", False, "30/01/20 17:00:00")
        e2 = Entry("192.168.11.1", False, "30/01/20 18:00:00")
        self.assertTrue( e1 < e2)


if __name__ == '__main__':
    unittest.main()
