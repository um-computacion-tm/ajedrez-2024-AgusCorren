from .piece import Piece

class Pawn(Piece):
    def __init__(self, color, position):
        self.__color__ = color
        self.__position__ = position

    def __str__(self):
        return "♙" if self.__color__ == "white" else "♟"
    
    def check_move(self, positions, new_position):


        x, y, current_x, current_y = self.get_coordinates(new_position)

        if self.__color__ == "white":
            return self.is_valid_white_move(x, y, current_x, current_y, positions)
        elif self.__color__ == "black":
            return self.is_valid_black_move(x, y, current_x, current_y, positions)

        return False
    
    def is_valid_white_move(self, x, y, current_x, current_y, positions):

        result = False

        if y == current_y:
                if current_x == 6:
                    if x == current_x - 1 and positions[current_x - 1][current_y] is None:
                        result = True
                    elif x == current_x - 2 and positions[current_x - 1][current_y] is None and positions[current_x - 2][current_y] is None:
                        result = True
                elif x == current_x - 1 and positions[current_x - 1][current_y] is None:
                    result = True
            # Movimiento de captura
        elif x == current_x - 1 and abs(y - current_y) == 1 and positions[x][y] is not None:
            result = True

        return result
    
    def is_valid_black_move(self, x, y, current_x, current_y, positions):

        result = False

        if y == current_y:
                if current_x == 1:
                    if x == current_x + 1 and positions[current_x + 1][current_y] is None:
                        result = True
                    elif x == current_x + 2 and positions[current_x + 1][current_y] is None and positions[current_x + 2][current_y] is None:
                        result = True
                elif x == current_x + 1 and positions[current_x + 1][current_y] is None:
                    result = True
        # Movimiento de captura
        elif x == current_x + 1 and abs(y - current_y) == 1 and positions[x][y] is not None:
            result = True
        return result