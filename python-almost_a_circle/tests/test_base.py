#!/usr/bin/python3
"""Unittest for Almost a circle project"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    def test_id(self):
        # Check if ID is greater than 0
        base = Base()
        self.assertGreater(base.id, 0)

    def test_id_increment(self):
        # Check if ID is equal to the previous + 1
        base1 = Base()
        base2 = Base()
        
        self.assertEqual(base2.id, base1.id + 1)

    def test_id_saving(self):
        base = Base(89)
        
        self.assertEqual(base.id, 89)
