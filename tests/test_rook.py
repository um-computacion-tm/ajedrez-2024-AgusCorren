import unittest
from game.pieces.rook import Rook

class TestRook(unittest.TestCase):
    def setUp(self):
        # Configura un tablero vacío y una torre blanca en una posición inicial
        self.__positions__ = [[None] * 8 for _ in range(8)]
        self.__white_rook__ = Rook("white", (3, 3))
        self.__positions__[3][3] = self.__white_rook__

    def test_horizontal_move(self):
        # Prueba sin piezas bloqueando
        self.assertTrue(self.__white_rook__.check_move(self.__positions__, (3, 5)))
        # Pruebas con pieza bloqueando
        self.__positions__[3][4] = Rook("black", (3, 4))
        self.assertFalse(self.__white_rook__.check_move(self.__positions__, (3, 6)))

        self.__positions__[3][1] = Rook("black", (3, 1))
        self.assertFalse(self.__white_rook__.check_move(self.__positions__, (3, 0)))
    
    def test_vertical_move(self):
        # Prueba sin piezas bloqueando
        self.assertTrue(self.__white_rook__.check_move(self.__positions__, (5, 3)))
        # Pruebas con pieza bloqueando
        self.__positions__[4][3] = Rook("black", (4, 3))
        self.assertFalse(self.__white_rook__.check_move(self.__positions__, (6, 3)))

        self.__positions__[2][3] = Rook("black", (2, 3))
        self.assertFalse(self.__white_rook__.check_move(self.__positions__, (0, 3)))

    def test_set_position(self):
        # Prueba set_position
        self.__white_rook__.set_position((5, 5))
        self.assertEqual(self.__white_rook__.get_position(), (5, 5))

if __name__ == '__main__':
    unittest.main()