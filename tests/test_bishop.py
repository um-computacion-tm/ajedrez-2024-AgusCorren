import unittest
from game.pieces.bishop import Bishop

class TestBishop(unittest.TestCase):
    def setUp(self):
        # Configura un tablero vacío y un alfil blanco en una posición inicial
        self.__positions__ = [[None] * 8 for _ in range(8)]
        self.__white_bishop__ = Bishop("white", (4, 4))
        self.__positions__[4][4] = self.__white_bishop__

    def test_diagonal_move(self):
        # Pruebas sin piezas bloqueando
        self.assertTrue(self.__white_bishop__.check_move(self.__positions__, (6, 6)))

        self.assertTrue(self.__white_bishop__.check_move(self.__positions__, (2, 2)))

        # Pruebas con piezas bloqueando
        self.__positions__[3][3] = Bishop("black", (3, 3))
        self.assertFalse(self.__white_bishop__.check_move(self.__positions__, (1, 1)))

        self.__positions__[5][5] = Bishop("black", (5, 5))
        self.assertFalse(self.__white_bishop__.check_move(self.__positions__, (7, 7)))

    def test_invalid_move(self):
        # Prueba movimiento no diagonal
        self.assertFalse(self.__white_bishop__.check_move(self.__positions__, (4, 6)))
        self.assertFalse(self.__white_bishop__.check_move(self.__positions__, (6, 4)))  

    def test_set_position(self):
        # Prueba set_position
        self.__white_bishop__.set_position((5, 5))
        self.assertEqual(self.__white_bishop__.get_position(), (5, 5))



if __name__ == "__main__":
    unittest.main()