import unittest
from game.chess_game import Chess
from game.pieces.piece import Piece
from game.exceptions import *

class TestChess(unittest.TestCase):

    def setUp(self):
        self.chess = Chess()

    def test_move_valid(self):
        # Movimiento inicial válido de un peón
        self.assertTrue(self.chess.move(6, 0, 5, 0))
        # Asegurarse de que el turno cambie después de un movimiento válido
        self.assertEqual(self.chess.turn(), "BLACK")

    def test_move_invalid_position(self):
        # Movimiento a una posición fuera del tablero
        with self.assertRaises(InvalidPosition):
            self.chess.move(1, 0, 8, 0)

    def test_own_pieces(self):
        # Verificar que la pieza a mover es del mismo color que turno
        x, y = (6, 0)
        self.assertIsInstance(self.chess.own_pieces(x, y), Piece)
        x, y = (1, 0)
        with self.assertRaises(ColorError):
            self.chess.own_pieces(x, y)

    def test_turn_management(self):
        # Verificar el cambio de turnos
        self.assertEqual(self.chess.turn(), "WHITE")
        self.chess.change_turn()
        self.assertEqual(self.chess.turn(), "BLACK")
        self.chess.change_turn()
        self.assertEqual(self.chess.turn(), "WHITE")

    def test_validate_cords(self):
        # Validar coordenadas válidas
        self.assertTrue(self.chess.validate_cords(0, 0))
        self.assertTrue(self.chess.validate_cords(7, 7))

        # Validar coordenadas inválidas
        with self.assertRaises(InvalidPosition):
            self.chess.validate_cords(-1, 0)
        with self.assertRaises(InvalidPosition):
            self.chess.validate_cords(0, 8)

    def test_invalid_move(self):
        with self.assertRaises(PieceNotFoundError):
            self.chess.move(3, 0, 1, 0)
        with self.assertRaises(InvalidPieceMovement):
            self.chess.move(7, 1, 5, 4)

        with self.assertRaises(ColorError):
            self.chess.move(1, 0, 7, 1)
        
        with self.assertRaises(Exception):
            self.chess.move(7, 1, 7, 1)

if __name__ == "__main__":
    unittest.main()