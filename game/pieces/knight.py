from .piece import Piece

class Knight(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)

    def __str__(self):
        return "♘" if self.__color__ == "white" else "♞"
    
    def check_move(self, positions, new_position):

        x, y, current_x, current_y = self.get_coordinates(new_position)

        possible_moves = [
            (2, 1), (2, -1), (-2, 1), (-2, -1),
            (1, 2), (1, -2), (-1, 2), (-1, -2)
        ]

        for move in possible_moves:
            if (x, y) == (current_x + move[0], current_y + move[1]):
                return True
        return False