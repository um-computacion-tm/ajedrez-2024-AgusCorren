from .piece import Piece

class King(Piece):
    def __init__(self, color, position):
        self.__color__ = color
        self.__position__ = position
        
    def __str__(self):
        return "♚" if self.__color__ == "white" else "♔"
    
    def check_move(self, positions, new_position):

        x, y, current_x, current_y = self.get_coordinates(new_position)

        result = False

        if x == current_x + 1 or x == current_x - 1:
            if y == current_y or y == current_y + 1 or y == current_y - 1:
                result = True
        elif y == current_y + 1 or y == current_y - 1:
            if x == current_x or x == current_x + 1 or x == current_x - 1:
                result = True
        return result
