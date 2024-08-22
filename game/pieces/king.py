from .piece import Piece

class King(Piece):
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
        return "♚" if self.__color__ == "white" else "♔"
    
    def check_move(self, positions, new_position):
        x, y = new_position
        current_x, current_y = self.__position__

        if x == current_x + 1 or x == current_x - 1:
            if y == current_y or y == current_y + 1 or y == current_y - 1:
                return True
        elif y == current_y + 1 or y == current_y - 1:
            if x == current_x or x == current_x + 1 or x == current_x - 1:
                return True
        else:
            return False
