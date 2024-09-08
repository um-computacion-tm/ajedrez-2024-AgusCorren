import unittest
from game.chess_game import Chess
from game.pieces.piece import Piece
from game.pieces.pawn import Pawn
from game.pieces.king import King
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
    
    def test_cant_eat_king(self):
        # Verificar que las piezas no puedan comer al rey.
        self.__chess__.__board__.clean_board()
        self.__chess__.__board__.set_piece_on_board(5, 0, King("white", (5, 0)))
        self.__chess__.__board__.set_piece_on_board(2, 3, Pawn("white", (2, 3)))
        self.__chess__.__board__.set_piece_on_board(1, 0, Pawn("black", (1, 0)))
        self.__chess__.__board__.set_piece_on_board(1, 4, King("black", (1, 4)))
        with self.assertRaises(CantEatKingError):
            self.__chess__.move("D2", "E1")

    def test_invalid_move(self):
        with self.assertRaises(PieceNotFoundError):
            self.__chess__.move("A3", "A1")
        with self.assertRaises(InvalidPieceMovement):
            self.__chess__.move("B7", "E4")

        with self.assertRaises(ColorError):
            self.__chess__.move("A1", "B2")
        
        with self.assertRaises(Exception):
            self.__chess__.move("A7", "A7")

    def test_check_victory(self):
        # Simular una victoria blanca
        self.__chess__.__board__.clean_board()
        self.__chess__.change_turn()
        self.__chess__.__board__.set_piece_on_board(5, 0, Pawn("white", (5, 0)))
        self.__chess__.__board__.set_piece_on_board(4, 0, King("white", (4, 0)))
        self.__chess__.__board__.set_piece_on_board(3, 0, King("black", (3, 0)))

        self.assertEqual(self.__chess__.check_victory(), "White wins")

        # Simular una victoria negra
        self.__chess__.__board__.clean_board()
        self.__chess__.change_turn()
        self.__chess__.__board__.set_piece_on_board(5, 0, Pawn("black", (5, 0)))
        self.__chess__.__board__.set_piece_on_board(4, 0, King("black", (4, 0)))
        self.__chess__.__board__.set_piece_on_board(3, 0, King("white", (3, 0)))

        self.assertEqual(self.__chess__.check_victory(), "Black wins")

        # Simular un empate
        self.__chess__.__board__.clean_board()
        self.__chess__.__board__.set_piece_on_board(4, 0, King("black", (4, 0)))
        self.__chess__.__board__.set_piece_on_board(1, 0, King("white", (1, 0)))

        self.__chess__.move("A1", "A2")

        self.assertEqual(self.__chess__.check_victory(), "Draw")

    def test_invalid_translate_input(self):
        with self.assertRaises(InvalidPosition):
            self.__chess__.translate_input("I9")  # Entrada fuera del rango válido
        with self.assertRaises(InvalidPosition):
            self.__chess__.translate_input("A9")  # Número de fila inválido
        with self.assertRaises(ValueError):
            self.__chess__.translate_input("A") # Debe tener dos caracteres
        with self.assertRaises(ValueError):
            self.__chess__.translate_input("AQ") # Columna inválida, debe ser un numero
        with self.assertRaises(ValueError): # Debe tener dos caracteres
            self.__chess__.move("A", "A")

    def test_move_status(self):
        # Prueba de EMPATE
        self.__chess__.__board__.clean_board()
        self.__chess__.__board__.set_piece_on_board(2, 0, Pawn("black", (2, 0)))
        self.__chess__.__board__.set_piece_on_board(4, 0, King("black", (4, 0)))
        self.__chess__.__board__.set_piece_on_board(1, 0, King("white", (1, 0)))
        self.assertEqual(self.__chess__.move("A1", "A2"), "Draw")

        # Prueba de Blancas ganan
        self.__chess__.__board__.clean_board()
        self.__chess__.change_turn()
        self.__chess__.__board__.set_piece_on_board(2, 0, Pawn("white", (2, 0)))
        self.__chess__.__board__.set_piece_on_board(4, 0, King("black", (4, 0)))
        self.__chess__.__board__.set_piece_on_board(1, 0, King("white", (1, 0)))
        self.assertEqual(self.__chess__.move("A4", "A3"), "White wins")

        # Prueba de Negras ganan
        self.__chess__.__board__.clean_board()
        self.__chess__.change_turn()
        self.__chess__.__board__.set_piece_on_board(2, 0, Pawn("black", (2, 0)))
        self.__chess__.__board__.set_piece_on_board(4, 0, King("white", (4, 0)))
        self.__chess__.__board__.set_piece_on_board(1, 0, King("black", (1, 0)))
        self.assertEqual(self.__chess__.move("A4", "A3"), "Black wins")

        # Prueba de empate
        self.__chess__.__board__.clean_board()
        self.__chess__.__board__.set_piece_on_board(2, 0, Pawn("black", (2, 0)))
        self.__chess__.__board__.set_piece_on_board(4, 0, King("black", (4, 0)))
        self.__chess__.__board__.set_piece_on_board(1, 0, King("white", (1, 0)))
        self.assertEqual(self.__chess__.move("A1", "A2"), "Draw")

    def test_next_turn(self):
        self.assertEqual(self.__chess__.next_turn(), "BLACK")
        self.__chess__.change_turn()
        self.assertEqual(self.__chess__.next_turn(), "WHITE")
if __name__ == "__main__":
    unittest.main()