import unittest
from game.board import Board
from game.pieces.rook import Rook
from game.pieces.pawn import Pawn
from game.pieces.bishop import Bishop
from game.pieces.knight import Knight
from game.pieces.king import King
from game.pieces.queen import Queen
from game.exceptions import InvalidMoveError, PieceNotFoundError, InvalidPieceMovement

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.__board__ = Board()

    def test_board_setup(self):
        # Verificar que los objetos de la clase Board se crean correctamente
        rook = self.__board__.get_piece(0, 0)
        knight = self.__board__.get_piece(0, 1)
        bishop = self.__board__.get_piece(0, 2)
        queen = self.__board__.get_piece(0, 3)
        king = self.__board__.get_piece(0, 4)
        pawn = self.__board__.get_piece(1, 0)

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
        # Verificar que get_piece devuelve la pieza correcta
        pawn_1 = self.__board__.get_piece(1, 0)
        self.assertIsNotNone(pawn_1)
        self.assertEqual(pawn_1.get_position(), (1, 0))
        for i in range(8):
            piece = self.__board__.get_piece(0, i)
            self.assertIsNotNone(piece)
            self.assertEqual(piece.get_position(), (0, i))

    def test_move_piece(self):
        # Verificar que move funcione correctamente
        origen = self.__board__.get_piece(1, 0)
        destino = (3, 0)
        self.__board__.move(origen, destino)
        moved_piece = self.__board__.get_piece(3, 0)
        self.assertEqual(moved_piece, origen)

    def test_piece_not_found(self):
        # Verificar el comportamiento al intentar mover una pieza que no existe
        empty_square = (4, 4)
        with self.assertRaises(PieceNotFoundError):
            self.__board__.move(self.__board__.get_piece(empty_square[0], empty_square[1]), (3, 3))

    def test_invalid_piece_movement(self):
        # Verificar que el tipo de movimiento de la pieza es valido
        origen_rook = self.__board__.get_piece(0, 0)
        destino_rook = (2, 2)
        with self.assertRaises(InvalidPieceMovement):
            self.__board__.move(origen_rook, destino_rook)

        origen_bishop = self.__board__.get_piece(0, 2)
        destino_bishop = (2, 2)
        with self.assertRaises(InvalidPieceMovement):
            self.__board__.move(origen_bishop, destino_bishop)
    
    def test_color_pieces(self):
        # Verificar que color_pieces devuelve el color correcto
        self.assertEqual(self.__board__.color_pieces(0, 0), "black")
        self.assertEqual(self.__board__.color_pieces(0, 1), "black")
        self.assertEqual(self.__board__.color_pieces(0, 2), "black")
        self.assertEqual(self.__board__.color_pieces(0, 3), "black")
        self.assertEqual(self.__board__.color_pieces(0, 4), "black")
        self.assertEqual(self.__board__.color_pieces(1, 0), "black")

        with self.assertRaises(PieceNotFoundError):
            self.__board__.color_pieces(5, 5)

        with self.assertRaises(PieceNotFoundError):
            self.__board__.color_pieces(4, 4)

    def test_move_with_no_piece(self):
        # Verificar el comportamiento al intentar mover sin una pieza en la posición inicial
        empty_square = (4, 4)
        destino = (5, 5)
        with self.assertRaises(PieceNotFoundError):
            self.__board__.move(self.__board__.get_piece(empty_square[0], empty_square[1]), destino)

    def test_execute_move(self):
        # Verificar que execute_move funcione correctamente
        origen = self.__board__.get_piece(6, 0)
        destino = (5, 0)
        self.__board__.execute_move(origen, destino)
        moved_piece = self.__board__.get_piece(5, 0)
        self.assertEqual(moved_piece, origen)
        self.assertIsNone(self.__board__.get_piece(6, 0))
        # Verificar que execute_move ha comido la pieza en el destino si es que tiene una
        origen2 = self.__board__.get_piece(7, 7)
        destino2 = (6, 7)
        piece_destino2 = self.__board__.get_piece(6, 7)
        self.__board__.execute_move(origen2, destino2)
        self.assertIsNone(piece_destino2.get_position())

    def test_find_piece(self):
        # Verificar que find_piece encuentre la pieza correcta
        origen = self.__board__.get_piece(0, 0)
        self.assertEqual(self.__board__.find_piece(origen), (0, 0))
        self.assertIsNone(self.__board__.find_piece(None))
        # Verificar que find_piece devuelve None si la pieza no está en el tablero
        piece_no_board = Rook("white", None)
        self.assertIsNone(self.__board__.find_piece(piece_no_board))

    def test_print_board(self):
        # Verificar que print_board no lance errores
        try:
            self.__board__.print_board()
        except Exception as e:
            self.fail(f"print_board raised an exception: {e}")

    def test_move_InvalidMoveError(self):
        origen = self.__board__.get_piece(7, 0)
        destino = (6, 0)
        with self.assertRaises(InvalidMoveError):
            self.__board__.move(origen, destino)

    def test_validate_move_PieceNotFoundError(self):
        piece_no_board = Rook("white", None)
        with self.assertRaises(PieceNotFoundError):
            self.__board__.validate_move(piece_no_board, (0, 0))

                            
if __name__ == "__main__":
    unittest.main()