# test_recursion.py

import unittest
from recursion import fibonacci, gcd, compareTo

class TestRecursionFunctions(unittest.TestCase):
    
    # Tests for Fibonacci
    def test_fibonacci(self):
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(10), 55)

    # Tests for GCD
    def test_gcd(self):
        self.assertEqual(gcd(48, 18), 6)
        self.assertEqual(gcd(100, 10), 10)
        self.assertEqual(gcd(17, 13), 1)
        self.assertEqual(gcd(0, 5), 5)

    # Tests for compareTo
    def test_compareTo(self):
        self.assertEqual(compareTo("abc", "abc"), 0)
        self.assertTrue(compareTo("abc", "abd") < 0)
        self.assertTrue(compareTo("abd", "abc") > 0)
        self.assertTrue(compareTo("", "a") < 0)
        self.assertTrue(compareTo("a", "") > 0)
        self.assertEqual(compareTo("", ""), 0)

if __name__ == "__main__":
    unittest.main()