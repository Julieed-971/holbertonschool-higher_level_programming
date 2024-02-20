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
