#!/usr/bin/python3
"""Unittest for Almost a circle project"""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_id(self):
        # Check if ID is greater than 0
        base = Base()
        self.assertGreater(base.id, 0)
