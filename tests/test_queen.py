import unittest
from game.pieces.queen import Queen

class TestQueen(unittest.TestCase):
    def setUp(self):
        self.__positions__ = [[None] * 8 for _ in range(8)]
        self.__white_queen__ = Queen("white", (4, 4))
        self.__positions__[4][4] = self.__white_queen__

    def test_diagonal_move(self):
        # Pruebas sin piezas bloqueando
        self.assertTrue(self.__white_queen__.check_move(self.__positions__, (6, 6)))
        self.assertTrue(self.__white_queen__.check_move(self.__positions__, (2, 2)))

        # Pruebas con piezas bloqueando
        self.__positions__[5][5] = Queen("black", (5, 5))
        self.assertFalse(self.__white_queen__.check_move(self.__positions__, (7, 7)))

        self.__positions__[3][3] = Queen("black", (3, 3))
        self.assertFalse(self.__white_queen__.check_move(self.__positions__, (1, 1)))

    def test_horizontal_move(self):
        # Pruebas sin piezas bloqueando
        self.assertTrue(self.__white_queen__.check_move(self.__positions__, (4, 6)))
        self.assertTrue(self.__white_queen__.check_move(self.__positions__, (4, 2)))

        # Pruebas con piezas bloqueando
        self.__positions__[4][5] = Queen("black", (4, 5))
        self.assertFalse(self.__white_queen__.check_move(self.__positions__, (4, 7)))

        self.__positions__[4][3] = Queen("black", (4, 3))
        self.assertFalse(self.__white_queen__.check_move(self.__positions__, (4, 1)))

    def test_vertical_move(self):
        # Pruebas sin piezas bloqueando
        self.assertTrue(self.__white_queen__.check_move(self.__positions__, (6, 4)))
        self.assertTrue(self.__white_queen__.check_move(self.__positions__, (2, 4)))

        # Pruebas con piezas bloqueando
        self.__positions__[5][4] = Queen("black", (5, 4))
        self.assertFalse(self.__white_queen__.check_move(self.__positions__, (7, 4)))

        self.__positions__[3][4] = Queen("black", (3, 4))
        self.assertFalse(self.__white_queen__.check_move(self.__positions__, (1, 4)))

    def test_invalid_move(self):
        # Movimiento no válido
        self.assertFalse(self.__white_queen__.check_move(self.__positions__, (5, 6)))  # Movimiento diagonal no permitido
        self.assertFalse(self.__white_queen__.check_move(self.__positions__, (6, 5)))  # Movimiento diagonal no permitido

    def test_set_position(self):
        self.__white_queen__.set_position((5, 5))
        self.assertEqual(self.__white_queen__.get_position(), (5, 5))

if __name__ == "__main__":
    unittest.main()