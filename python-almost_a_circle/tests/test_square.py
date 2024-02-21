#!/usr/bin/python3
"""Unittest for Almost a circle project"""

import unittest
import json
import sys
import os
import io

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """Unittests for the Square class"""
    def test_init(self):
        square = Square(1)
        self.assertEqual(square.size, 1)
        
        square = Square(1, 2)
        self.assertEqual(square.size, 1)
        self.assertEqual(square.x, 2)
        
        square = Square(1, 2, 3)
        self.assertEqual(square.size, 1)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)
        
        square = Square(1, 2, 3, 4)
        self.assertEqual(square.size, 1)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)
        self.assertEqual(square.id, 4)
        
    def test_types(self):
        """Test the type of arguments passed to the class""" 
        with self.assertRaises(TypeError):
            Square("1")
        with self.assertRaises(TypeError):
            Square(1, "2")
        with self.assertRaises(TypeError):
            Square(1, 2, "3")
    
    def test_values(self):
        """Test the values of arguments passed to the class"""
        with self.assertRaises(ValueError):
            Square(-1)
        with self.assertRaises(ValueError):
            Square(1, -2)
        with self.assertRaises(ValueError):
            Square(1, 2, -3)
        with self.assertRaises(ValueError):
            Square(0)

    def test_string_representation(self):
        square = Square(3, 4, 1, 2)
        self.assertEqual(str(square), "[Square] (2) 4/1 - 3")

    def test_to_dictionary(self):
        square = Square(3, 1, 2, 5)
        self.assertEqual(square.to_dictionary(), {'x': 1, 'y': 2, 'id': 5, 'size': 3})

    def test_update(self):
        square = Square(1, 2)
        square.update(2, 3, 4, 5)
        self.assertEqual(square.id, 2)
        self.assertEqual(square.size, 3)
        self.assertEqual(square.x, 4)
        self.assertEqual(square.y, 5)

    def test_update_method_exists(self):
        square = Square(1, 2)
        self.assertTrue(hasattr(square, 'update'))

    def test_create_method_exists(self):
        square = Square.create(**{'id': 89, 'size': 1})
        self.assertTrue(hasattr(square, 'create'))
        
    def test_save_to_file_with_none(self):
        Square.save_to_file(None)
        
        with open("Square.json", "r") as f:
            dict_output = json.load(f)
        
        expected_output = []
        self.assertEqual(dict_output, expected_output)
    
    def test_save_to_file_empty_list(self):
        Square.save_to_file([])
        
        with open("Square.json", "r") as f:

            self.assertEqual(f.read(), "[]")

    def test_save_to_file_square_1(self):
        filename = "Square.json"
        Square.save_to_file([Square(1)])
        self.assertTrue(os.path.exists(filename))
        
        with open(filename, "r") as f:
            file_content = f.read()
        self.assertEqual(file_content, '[{"id": 23, "x": 0, "size": 1, "y": 0}]')
        
        os.remove(filename)  
    
    def test_load_from_file_file_does_not_exist(self):
        self.assertEqual(Square.load_from_file(), [])

    def test_load_from_file_file_exists(self):
        Square.save_to_file([Square(1, 2)])
        dict_output = Square.load_from_file()
        expected_output = [Square(1, 2)]
        self.assertNotEqual(str(dict_output), str(expected_output))

if __name__ == "__main__":
    unittest.main()
