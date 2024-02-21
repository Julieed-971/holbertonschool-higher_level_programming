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
        
        square1 = Square(1, 2, 3, 4)
        self.assertEqual(square1.size, 1)
        self.assertEqual(square1.x, 2)
        self.assertEqual(square1.y, 3)
        self.assertEqual(square1.id, 4)
        
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
        filename = "square.json"
        Square.save_to_file([])
        self.assertTrue(os.path.exists(filename))
        
        with open(filename, "r") as f:
            file_content = f.read()
            print("File content:", file_content)
        
        file_size = os.path.getsize(filename)
        self.assertGreater(file_size, 0)
        
        os.remove(filename)
    
    def test_save_to_file_empty_list(self):
        filename = "Square.json"
        Square.save_to_file([])
        self.assertTrue(os.path.exists(filename))
        
        with open(filename, "r") as f:
            file_content = f.read()
        self.assertEqual(file_content, "[]")
        
        os.remove(filename)
    
    def test_load_from_file_file_does_not_exist(self):
        self.assertEqual(Square.load_from_file(), [])

    def test_load_from_file_file_exists(self):
        Square.save_to_file([Square(1, 2)])
        dict_output = Square.load_from_file()
        expected_output = [Square(1, 2)]
        self.assertNotEqual(str(dict_output), str(expected_output))

# Test of Square(1) exists

# Test of Square(1, 2) exists

# Test of Square(1, 2, 3) exists

# Test of Square("1") exists

# Test of Square(1, "2") exists

# Test of Square(1, 2, "3") exists

# Test of Square(1, 2, 3, 4) exists

# Test of Square(-1) exists

# Test of Square(1, -2) exists

# Test of Square(1, 2, -3) exists

# Test of Square(0) exists

# Test of __str__() for Square exists

# Test of to_dictionary() in Square exists

# Test of update() in Square exists

# Test of update(89) in Square exists

# Test of update(89, 1) in Square exists

# Test of update(89, 1, 2) in Square exists

# Test of update(89, 1, 2, 3) in Square exists

# Test of update(**{ 'id': 89 }) in Square exists

# Test of update(**{ 'id': 89, 'size': 1 }) in Square exists

# Test of update(**{ 'id': 89, 'size': 1, 'x': 2 }) in Square exists

# Test of update(**{ 'id': 89, 'size': 1, 'x': 2, 'y': 3 }) in Square exists

# Test of Square.create(**{ 'id': 89 }) in Square exists

# Test of Square.create(**{ 'id': 89, 'size': 1 }) in Square exists

# Test of Square.create(**{ 'id': 89, 'size': 1, 'x': 2 }) in Square exists

# Test of Square.create(**{ 'id': 89, 'size': 1, 'x': 2, 'y': 3 }) in Square exists

# Test of Square.save_to_file(None) in Square exists

# Test of Square.save_to_file([]) in Square exists

# Test of Square.save_to_file([Square(1)]) in Square exists

# Test of Square.load_from_file() when file doesn’t exist exists

# Test of Square.load_from_file() when file exists exists
