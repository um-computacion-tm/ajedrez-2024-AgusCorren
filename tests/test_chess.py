import unittest
from game.chess_game import Chess
from game.pieces.piece import Piece
from game.exceptions import *

class TestChess(unittest.TestCase):

    def setUp(self):
        self.__chess__ = Chess()

    def test_move_valid(self):
        # Movimiento inicial válido de un peón
        self.assertTrue(self.__chess__.move("A6", "A5"))
        # Asegurarse de que el turno cambie después de un movimiento válido
        self.assertEqual(self.__chess__.turn(), "BLACK")

    def test_move_invalid_position(self):
        # Movimiento a una posición fuera del tablero
        with self.assertRaises(InvalidPosition):
            self.__chess__.move("A1", "A8")

    def test_own_pieces(self):
        # Verificar que la pieza a mover es del mismo color que turno
        self.assertIsInstance(self.__chess__.own_pieces(6, 0), Piece)
        with self.assertRaises(ColorError):
            self.__chess__.own_pieces(1, 0)

    def test_turn_management(self):
        # Verificar el cambio de turnos
        self.assertEqual(self.__chess__.turn(), "WHITE")
        self.__chess__.change_turn()
        self.assertEqual(self.__chess__.turn(), "BLACK")
        self.__chess__.change_turn()
        self.assertEqual(self.__chess__.turn(), "WHITE")

    def test_invalid_move(self):
        with self.assertRaises(PieceNotFoundError):
            self.__chess__.move("A3", "A1")
        with self.assertRaises(InvalidPieceMovement):
            self.__chess__.move("B7", "E4")

        with self.assertRaises(ColorError):
            self.__chess__.move("A1", "B2")
        
        with self.assertRaises(Exception):
            self.__chess__.move("A7", "A7")

if __name__ == "__main__":
    unittest.main()