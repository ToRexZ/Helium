import unittest
import sys

sys.path.append('./heliumrewards')

import HeliumData


class TestJsonDataFetch(unittest.TestCase):
    def testFetchPreviousData(self):
        result = HeliumData.fetchPreviousData()
        resultDataType = type(result)
        self.assertEqual(resultDataType,type(0),"Should be integer")


if __name__ == '__main__':
    unittest.main()
        