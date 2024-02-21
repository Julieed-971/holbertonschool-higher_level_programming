#!/usr/bin/python3
"""Unittest for Almost a circle project"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Test the Base class"""
    def test_id(self):
        """Check if ID is greater than 0"""
        base = Base()
        self.assertGreater(base.id, 0)

    def test_id_increment(self):
        """Check if ID is equal to the previous + 1"""
        base1 = Base()
        base2 = Base()
        
        self.assertEqual(base2.id, base1.id + 1)

    def test_id_saving(self):
        """Check if the id is saved correctly"""
        base = Base(89)
        
        self.assertEqual(base.id, 89)
    
    def test_to_json_string_none(self):
        """Check if method returns '[]' when input is None."""
        base = Base.to_json_string(None)
        self.assertEqual(base, "[]")

    def test_to_json_string_empty_list(self):
        """Check if method returns '[]' when input is empty list."""
        base = Base.to_json_string([])
        self.assertEqual(base, "[]")

    def test_to_json_string_single_object(self):
        """Check if method returns string representation of single object."""
        base = Base.to_json_string([{'id': 12}])
        self.assertEqual(base, '[{"id": 12}]')

    def test_from_json_string_none(self):
        """Check if method returns empty list when input is None."""
        base = Base.from_json_string(None)
        self.assertEqual(base, [])

    def test_from_json_string_empty_string(self):
        """Check if method returns empty list when input is empty string."""
        base = Base.from_json_string("[]")
        self.assertEqual(base, [])

    def test_from_json_string_single_object(self):
        """Check if method returns a list containing a single object."""
        base = Base.from_json_string('[{"id": 89}]')
        self.assertEqual(base, [{"id": 89}]) 

if __name__ == "__main__":
    unittest.main()