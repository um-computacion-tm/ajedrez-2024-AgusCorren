import unittest
from game.pieces.knight import Knight

class TestKnight(unittest.TestCase):
    def setUp(self):
        self.__positions__ = [[None] * 8 for _ in range(8)]
        self.__knight__ = Knight("white", (4, 4))
        self.__positions__[4][4] = self.__knight__

    def test_white_knight_moves(self):
        # Verificar todos los movimientos posibles del caballo
        self.assertTrue(self.__knight__.check_move(self.__positions__, (6, 3)))
        self.assertTrue(self.__knight__.check_move(self.__positions__, (6, 5)))
        self.assertTrue(self.__knight__.check_move(self.__positions__, (2, 3)))
        self.assertTrue(self.__knight__.check_move(self.__positions__, (2, 5)))
        self.assertTrue(self.__knight__.check_move(self.__positions__, (5, 2)))
        self.assertTrue(self.__knight__.check_move(self.__positions__, (3, 2)))
        self.assertTrue(self.__knight__.check_move(self.__positions__, (5, 6)))
        self.assertTrue(self.__knight__.check_move(self.__positions__, (3, 6)))

    def test_white_knight_invalid_moves(self):
        # Verificar movimiento no válido del caballo
        self.assertFalse(self.__knight__.check_move(self.__positions__, (5, 5)))

    def test_set_position(self):
        self.__knight__.set_position((5, 5))
        self.assertEqual(self.__knight__.get_position(), (5, 5))

if __name__ == "__main__":
    unittest.main()