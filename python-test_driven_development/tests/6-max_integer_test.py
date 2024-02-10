#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_types(self):
        # Make sure types errors are raised when necessary
        self.assertRaises(TypeError, max_integer, set)
        self.assertRaises(TypeError, max_integer, [1, 2, 3, 4], [1, 3, 4, 2])
        self.assertRaises(TypeError, max_integer, (1, 3), (4, 2))
        self.assertRaises(TypeError, max_integer, '1, 3', '4, 2')
        
    def test_values(self):
        # Test the values passed to the function
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)
        self.assertEqual(max_integer([1, 4, 1, 4]), 4)
        self.assertEqual(max_integer([3, 3, 3, 3]), 3)
        self.assertEqual(max_integer([1.5, 2.5, 3.5, 4.5]), 4.5)
        self.assertEqual(max_integer((1, 3, 4, 2)), 4)
        self.assertEqual(max_integer([None]), None)
        self.assertEqual(max_integer("abcdef"), 'f')
                         
        
        
        
        