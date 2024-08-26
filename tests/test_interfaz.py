import unittest
from unittest.mock import patch
from game.interfaz import Interfaz

class TestInterfaz(unittest.TestCase):
    def setUp(self):
        self.__interfaz__ = Interfaz()

    def test_menu(self):
        ...


'''
En proceso
'''

if __name__ == '__main__':
    unittest.main()