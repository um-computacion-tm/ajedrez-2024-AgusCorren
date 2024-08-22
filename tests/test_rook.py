import unittest
from game.pieces.rook import Rook

class TestRook(unittest.TestCase):
    def setUp(self):
        # Configura un tablero vacío y una torre blanca en una posición inicial
        self.positions = [[None] * 8 for _ in range(8)]
        self.white_rook = Rook("white", (3, 3))
        self.positions[3][3] = self.white_rook

    def test_horizontal_move(self):
        # Prueba movimiento horizontal hacia la derecha sin piezas bloqueando
        self.assertTrue(self.white_rook.check_move(self.positions, (3, 5)))
        # Prueba movimiento horizontal hacia la derecha con pieza bloqueando
        self.positions[3][4] = Rook("black", (3, 4))
        self.assertFalse(self.white_rook.check_move(self.positions, (3, 6)))
        # Prueba movimiento horizontal hacia la izquierda con pieza bloqueando
        self.positions[3][1] = Rook("black", (3, 1))
        self.assertFalse(self.white_rook.check_move(self.positions, (3, 0)))
    
    def test_vertical_move(self):
        # Prueba movimiento vertical hacia arriba sin piezas bloqueando
        self.assertTrue(self.white_rook.check_move(self.positions, (5, 3)))
        # Prueba movimiento vertical hacia arriba con pieza bloqueando
        self.positions[4][3] = Rook("black", (4, 3))
        self.assertFalse(self.white_rook.check_move(self.positions, (6, 3)))
        # Prueba movimiento vertical hacia abajo con pieza bloqueando
        self.positions[2][3] = Rook("black", (2, 3))
        self.assertFalse(self.white_rook.check_move(self.positions, (0, 3)))

    def test_set_position(self):
        # Prueba set_position
        self.white_rook.set_position((5, 5))
        self.assertEqual(self.white_rook.get_position(), (5, 5))

if __name__ == '__main__':
    unittest.main()
