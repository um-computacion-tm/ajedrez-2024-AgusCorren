from .piece import Piece

class Bishop(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
    
    def get_color(self):
        return super().get_color()