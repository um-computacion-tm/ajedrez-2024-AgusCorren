import unittest
from game.board import Board
from game.pieces.rook import Rook
from game.pieces.pawn import Pawn
from game.pieces.bishop import Bishop
from game.pieces.knight import Knight
from game.pieces.king import King
from game.pieces.queen import Queen
from game.exceptions import InvalidMoveError, PieceNotFoundError

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()

    def test_board_setup(self):
        rook = self.board.get_piece(0, 0)
        knight = self.board.get_piece(0, 1)
        bishop = self.board.get_piece(0, 2)
        queen = self.board.get_piece(0, 3)
        king = self.board.get_piece(0, 4)
        pawn = self.board.get_piece(1, 0)

        self.assertIsInstance(pawn, Pawn)
        self.assertIsInstance(rook, Rook)
        self.assertIsInstance(bishop, Bishop)
        self.assertIsInstance(knight, Knight)
        self.assertIsInstance(king, King)
        self.assertIsInstance(queen, Queen)
        
        self.assertEqual(rook.get_color(), "black")
        self.assertEqual(pawn.get_color(), "black")
        self.assertEqual(bishop.get_color(), "black")
        self.assertEqual(knight.get_color(), "black")
        self.assertEqual(king.get_color(), "black")
        self.assertEqual(queen.get_color(), "black")

    def test_get_piece(self):
        piece = self.board.get_piece(1, 0)
        self.assertIsNotNone(piece)
        self.assertEqual(piece.get_position(), (1, 0))

    def test_move_piece(self):
        origen = self.board.get_piece(1, 0)
        destino = (3, 0)
        self.board.move(origen, destino)
        moved_piece = self.board.get_piece(3, 0)
        self.assertEqual(moved_piece, origen)

    def test_invalid_move(self):
        origen = self.board.get_piece(1, 0)
        destino = (1, 1)
        with self.assertRaises(InvalidMoveError):
            self.board.move(origen, destino)

    def test_piece_not_found(self):
        empty_square = (4, 4)
        with self.assertRaises(PieceNotFoundError):
            self.board.move(self.board.get_piece(empty_square[0], empty_square[1]), (3, 3))

if __name__ == "__main__":
    unittest.main()