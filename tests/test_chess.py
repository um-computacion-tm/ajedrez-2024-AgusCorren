import unittest
from game.chess_game import Chess
from game.pieces.piece import Piece
from game.exceptions import *

class TestChess(unittest.TestCase):

    def setUp(self):
        self.__chess__ = Chess()

    def test_move_valid(self):
        # Movimiento inicial válido de un peón
        self.assertTrue(self.__chess__.move(6, 0, 5, 0))
        # Asegurarse de que el turno cambie después de un movimiento válido
        self.assertEqual(self.__chess__.turn(), "BLACK")

    def test_move_invalid_position(self):
        # Movimiento a una posición fuera del tablero
        with self.assertRaises(InvalidPosition):
            self.__chess__.move(1, 0, 8, 0)

    def test_own_pieces(self):
        # Verificar que la pieza a mover es del mismo color que turno
        x, y = (6, 0)
        self.assertIsInstance(self.__chess__.own_pieces(x, y), Piece)
        x, y = (1, 0)
        with self.assertRaises(ColorError):
            self.__chess__.own_pieces(x, y)

    def test_turn_management(self):
        # Verificar el cambio de turnos
        self.assertEqual(self.__chess__.turn(), "WHITE")
        self.__chess__.change_turn()
        self.assertEqual(self.__chess__.turn(), "BLACK")
        self.__chess__.change_turn()
        self.assertEqual(self.__chess__.turn(), "WHITE")

    def test_validate_cords(self):
        # Validar coordenadas válidas
        self.assertTrue(self.__chess__.validate_cords(0, 0))
        self.assertTrue(self.__chess__.validate_cords(7, 7))

        # Validar coordenadas inválidas
        with self.assertRaises(InvalidPosition):
            self.__chess__.validate_cords(-1, 0)
        with self.assertRaises(InvalidPosition):
            self.__chess__.validate_cords(0, 8)

    def test_invalid_move(self):
        with self.assertRaises(PieceNotFoundError):
            self.__chess__.move(3, 0, 1, 0)
        with self.assertRaises(InvalidPieceMovement):
            self.__chess__.move(7, 1, 5, 4)

        with self.assertRaises(ColorError):
            self.__chess__.move(1, 0, 7, 1)
        
        with self.assertRaises(Exception):
            self.__chess__.move(7, 1, 7, 1)

if __name__ == "__main__":
    unittest.main()