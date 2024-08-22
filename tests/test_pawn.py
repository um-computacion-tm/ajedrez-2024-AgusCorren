import unittest
from game.pieces.pawn import Pawn

class TestPawn(unittest.TestCase):
    def setUp(self):
        self.__positions__ = [[None] * 8 for _ in range(8)]
        # Peones blancos en la fila 6 y peones negros en la fila 1
        self.__white_pawn__ = Pawn("white", (6, 4))
        self.__black_pawn__ = Pawn("black", (1, 4))
        self.__white_pawn2__ = Pawn("white", (4, 2))
        self.__black_pawn2__ = Pawn("black", (2, 6))
        self.__positions__[6][4] = self.__white_pawn__
        self.__positions__[1][4] = self.__black_pawn__
        self.__positions__[2][2] = self.__white_pawn2__
        self.__positions__[4][6] = self.__black_pawn2__

    def test_white_pawn_moves(self):
        # Movimiento hacia adelante sin captura
        self.assertTrue(self.__white_pawn__.check_move(self.__positions__, (5, 4)))  # Avance 1 casilla en posicion inicial
        self.assertTrue(self.__white_pawn__.check_move(self.__positions__, (4, 4)))  # Avance 2 casillas 
        self.assertTrue(self.__white_pawn2__.check_move(self.__positions__, (3, 2))) # Avance 1 casilla en posicion no inicial
        
        # Movimiento de captura
        self.__positions__[5][5] = Pawn("black", (5, 5))  # Oponente a comer
        self.assertTrue(self.__white_pawn__.check_move(self.__positions__, (5, 5)))
        
        self.__positions__[5][3] = Pawn("black", (5, 3))  # Oponente a comer
        self.assertTrue(self.__white_pawn__.check_move(self.__positions__, (5, 3)))
        
        # Movimiento inválido
        self.__positions__[5][4] = Pawn("black", (5, 4))
        self.assertFalse(self.__white_pawn__.check_move(self.__positions__, (4, 4)))  # Movimiento hacia adelante cuando la casilla está ocupada
        self.assertFalse(self.__white_pawn__.check_move(self.__positions__, (6, 6)))  # Movimiento en una dirección no válida

    def test_black_pawn_moves(self):
        # Movimiento hacia adelante sin captura
        self.assertTrue(self.__black_pawn__.check_move(self.__positions__, (2, 4)))  # Avance 1 casilla en posicion inicial
        self.assertTrue(self.__black_pawn__.check_move(self.__positions__, (3, 4)))  # Avance 2 casillas
        self.assertTrue(self.__black_pawn2__.check_move(self.__positions__, (3, 6))) # Avance 1 casilla en posicion no inicial
        
        # Movimiento de captura
        self.__positions__[2][5] = Pawn("white", (2, 5))  # Oponente a comer
        self.assertTrue(self.__black_pawn__.check_move(self.__positions__, (2, 5)))
        
        self.__positions__[2][3] = Pawn("white", (2, 3))  # Oponente a comer
        self.assertTrue(self.__black_pawn__.check_move(self.__positions__, (2, 3)))
        
        # Movimiento inválido
        self.__positions__[2][4] = Pawn("white", (2, 4))
        self.assertFalse(self.__black_pawn__.check_move(self.__positions__, (3, 4)))  # Movimiento hacia adelante cuando la casilla está ocupada
        self.assertFalse(self.__black_pawn__.check_move(self.__positions__, (1, 1)))  # Movimiento en una dirección no válida

    def test_set_position(self):
        self.__white_pawn__.set_position((5, 5))
        self.assertEqual(self.__white_pawn__.get_position(), (5, 5))
        self.__black_pawn__.set_position((2, 5))
        self.assertEqual(self.__black_pawn__.get_position(), (2, 5))


if __name__ == "__main__":
    unittest.main()