import unittest
from game.chess_game import Chess
from game.exceptions import PieceNotFoundError, InvalidMoveError, InvalidPosition

class TestChess(unittest.TestCase):

    def setUp(self):
        self.chess = Chess()

    def test_move_valid(self):
        # Movimiento inicial válido de un peón
        self.assertTrue(self.chess.move(1, 0, 2, 0))
        # Asegurarse de que el turno cambie después de un movimiento válido
        self.assertEqual(self.chess.turn(), "BLACK")

    def test_move_invalid_position(self):
        # Movimiento a una posición fuera del tablero
        with self.assertRaises(InvalidPosition):
            self.chess.move(1, 0, 8, 0)

    def test_is_a_piece(self):
        # Verificar que existe una pieza en la posición inicial
        piece = self.chess.is_a_piece(0, 0)
        self.assertIsNotNone(piece)
        
        # Verificar que no exista una pieza en una posición vacía
        with self.assertRaises(PieceNotFoundError):
            self.chess.is_a_piece(4, 4)

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

if __name__ == "__main__":
    unittest.main()