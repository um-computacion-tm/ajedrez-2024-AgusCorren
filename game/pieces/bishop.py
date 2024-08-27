from .piece import Piece

class Bishop(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)

    def __str__(self):
        return "♗" if self.__color__ == "white" else "♝"
    
    def check_move(self, positions, new_position):

        if self.diagonal_move(positions, new_position):
            return True
        return False