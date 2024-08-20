from .piece import Piece
from game.exceptions import InvalidPieceMovement

class Rook(Piece):
    def __init__(self, color, position):
        self.__color__ = color
        self.__position__ = position
    
    def get_color(self):
        return self.__color__
    
    def get_position(self):
        return self.__position__

    def set_position(self, new_position):
        self.__position__ = new_position

    def __str__(self):
        return "♖" if self.__color__ == "white" else "♜"
    
    def check_move(self, new_position):
        x, y = new_position
        current_x, current_y = self.__position__

        if x == current_x and y != current_y:
            return True
        elif x != current_x and y == current_y:
            return True
        else:
            return False