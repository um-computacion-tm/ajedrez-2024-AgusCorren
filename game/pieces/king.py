from .piece import Piece

class King(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        
    def __str__(self):
        return "♚" if self.__color__ == "white" else "♔"
    
    def check_move(self, positions, new_position):

        x, y, current_x, current_y = self.get_coordinates(new_position)

        if abs(x - current_x) <= 1 and abs(y - current_y) <= 1:
            return True
        return False