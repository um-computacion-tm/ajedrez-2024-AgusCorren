import unittest
from game.pieces.king import King

class TestKing(unittest.TestCase):
    def setUp(self):
        self.__positions__ = [[None] * 8 for _ in range(8)]
        self.__white_king__ = King("white", (4, 4))
        self.__positions__[4][4] = self.__white_king__

    def test_valid_moves(self):
        # Movimiento válido en todas las direcciones
        self.assertTrue(self.__white_king__.check_move(self.__positions__, (5, 5)))
        self.assertTrue(self.__white_king__.check_move(self.__positions__, (5, 4)))
        self.assertTrue(self.__white_king__.check_move(self.__positions__, (5, 3)))
        self.assertTrue(self.__white_king__.check_move(self.__positions__, (4, 5)))
        self.assertTrue(self.__white_king__.check_move(self.__positions__, (4, 3)))
        self.assertTrue(self.__white_king__.check_move(self.__positions__, (3, 5)))
        self.assertTrue(self.__white_king__.check_move(self.__positions__, (3, 4)))
        self.assertTrue(self.__white_king__.check_move(self.__positions__, (3, 3)))

    def test_invalid_moves(self):
        # Movimiento inválido (más de una casilla)
        self.assertFalse(self.__white_king__.check_move(self.__positions__, (6, 6)))
        self.assertFalse(self.__white_king__.check_move(self.__positions__, (2, 2)))
        self.assertFalse(self.__white_king__.check_move(self.__positions__, (6, 4)))
        self.assertFalse(self.__white_king__.check_move(self.__positions__, (4, 6)))

    def test_set_position(self):
        self.__white_king__.set_position((5, 5))
        self.assertEqual(self.__white_king__.get_position(), (5, 5))

if __name__ == "__main__":
    unittest.main()