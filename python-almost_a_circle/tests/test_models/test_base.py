#!/usr/bin/python3
"""Unittest for Almost a circle project"""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_id(self):
        # Create multiple instances of Base
        base = Base()
        
        # Check if instance has an ID attribute
        self.assertTrue(hasattr(base, 'id'))

        # Check if ID is an integer
        self.assertIsInstance(base.id, int)
        
        # Check if ID is greater than or equal to 1
        self.assertGreaterEqual(base.id, 1)