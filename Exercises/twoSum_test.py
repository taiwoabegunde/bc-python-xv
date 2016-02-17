import unittest

from twoSum import twoSum

class TwoSumTestSuite(unittest.TestCase):

    def test_list_range_4(self):

        result = twoSum([2,5,1,7], 8)

        self.assertEqual(result, [2,3])

    def test_list_range_10(self):

        result = twoSum([4,6,5,13,11,32,30,2,7,10], 43)

        self.assertEqual(result, [3, 6])

    def test_list_range_same(self):

        result = twoSum([4,6,6,6,32,8], 12)

        self.assertEqual(result, [0, 5])

    def test_list_range_8(self):

        result = twoSum([4,6,5,2,15,12,33,12], 37)

        self.assertEqual(result, [0, 6])

    def test_list_range_7(self):

        result = twoSum([4,6,5,13,11,32,30,2,7,10], 37)

        self.assertEqual(result, [2, 5])

    def test_list_range_15(self):

        result = twoSum([3,30,21,25,11,66,32,10,29,1,12,23,45,56,4], 34)

        self.assertEqual(result, [1, 14])

    def test_list_range_20(self):

        result = twoSum([4,6,5,13,11,32,30,2,7,10,11,66,32,10,29,1,12,23,19,51], 39)

        self.assertEqual(result, [5, 8])

    def test_list_range_12(self):

        result = twoSum([3,21,25,10,29,1,12,23,45,56,4,45], 49)

        self.assertEqual(result, [8, 10])

    def test_list_range_17(self):

        result = twoSum([3,30,21,25,11,66,32,10,29,45,56,4,13,11,32,30,2], 75)

        self.assertEqual(result, [1, 9])

    def test_list_range_19(self):

        result = twoSum([3,30,21,25,11,66,32,10,29,45,56,4,13,11,32,30,2], 55)

        self.assertEqual(result, [1, 3])

if __name__== "__main__":

    unittest.main()