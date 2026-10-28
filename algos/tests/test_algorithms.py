import unittest

from src.is_palindrome import is_palindrome
from src.longest_palindrome import find_longest_palindrome
from src.missing_number import missing_number
from src.product_except_self import product_except_self
from src.rob_rooms import rob


class TestAlgorithms(unittest.TestCase):
    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))
        self.assertFalse(is_palindrome("race a car"))
        self.assertTrue(is_palindrome("!!!"))

    def test_longest_palindrome(self):
        self.assertEqual(find_longest_palindrome("abba"), "abba")
        self.assertIn(find_longest_palindrome("babad"), ("bab", "aba"))
        self.assertEqual(find_longest_palindrome(""), "")

    def test_missing_number(self):
        self.assertEqual(missing_number([3, 0, 1]), 2)
        self.assertEqual(missing_number([0, 1]), 2)
        self.assertEqual(missing_number([]), 0)

    def test_product_except_self(self):
        self.assertEqual(product_except_self([1, 2, 3, 4]), [24, 12, 8, 6])
        self.assertEqual(product_except_self([-1, 1, 0, -3, 3]), [0, 0, 9, 0, 0])

    def test_rob(self):
        self.assertEqual(rob([5, 1, 1, 5]), 10)
        self.assertEqual(rob([2, 7, 9, 3, 1]), 12)
        self.assertEqual(rob([]), 0)


if __name__ == "__main__":
    unittest.main()
