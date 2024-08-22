import unittest
from game.pieces.piece import Piece

class TestPiece(unittest.TestCase):
    def setUp(self):
        self.__pieza__ = Piece("white", (4, 4))

    def test_get_color(self):
        self.assertEqual(self.__pieza__.get_color(), "white")

    def test_get_position(self):
        self.assertEqual(self.__pieza__.get_position(), (4, 4))

    def test_set_position(self):
        self.__pieza__.set_position((5, 5))
        self.assertEqual(self.__pieza__.get_position(), (5, 5))
    
    def test_check_move(self):
        self.assertTrue(self.__pieza__.check_move(None, None))
    
if __name__ == "__main__":
    unittest.main()