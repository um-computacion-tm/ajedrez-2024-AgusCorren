from .piece import Piece

class Rook(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)

    def __str__(self):
        return "♖" if self.__color__ == "white" else "♜"
    
    def check_move(self, positions, new_position):
        
        if self.horizontal_move(positions, new_position) or self.vertical_move(positions, new_position):
            return True
        return False