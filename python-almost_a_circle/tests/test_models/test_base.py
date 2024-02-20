#!/usr/bin/python3
"""Unittest for Almost a circle project"""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_id(self):
        # Create multiple instances of Base
        base1 = Base()
        base2 = Base()
        base3 = Base()

        # Check if each instance has a unique ID
        self.assertNotEqual(base1.id, base2.id)
        self.assertNotEqual(base1.id, base3.id)
        self.assertNotEqual(base2.id, base3.id)
