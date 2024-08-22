import unittest
from unittest.mock import patch
from game.interfaz import Interfaz

class TestInterfaz(unittest.TestCase):
    def setUp(self):
        self.__interfaz__ = Interfaz()
    
    def test_validate_option(self):
        self.assertEqual(self.__interfaz__.validate_option('3'), "Invalid option")
        self.assertEqual(self.__interfaz__.validate_option('1'), "Game Started")
        self.assertEqual(self.__interfaz__.validate_option('2'), "Game Over")

    def test_menu(self):
        ...


'''
En proceso
'''

if __name__ == '__main__':
    unittest.main()