import unittest

from twoSum_using_dictionary import twoSum

class TwoSumTestSuite(unittest.TestCase):

    def test_list_range_17(self):
        result = twoSum([5,6,10,1,2], 3)

        self.assertEqual(result, [3, 4])

if __name__== "__main__":

    unittest.main()