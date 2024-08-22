from .piece import Piece

class Knight(Piece):
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
        return "♘" if self.__color__ == "white" else "♞"
    
    def check_move(self, positions, new_position):
        x, y = new_position
        current_x, current_y = self.__position__

        possible_moves = [
            (2, 1), (2, -1), (-2, 1), (-2, -1),
            (1, 2), (1, -2), (-1, 2), (-1, -2)
        ]

        for move in possible_moves:
            if (x, y) == (current_x + move[0], current_y + move[1]):
                return True

        return False