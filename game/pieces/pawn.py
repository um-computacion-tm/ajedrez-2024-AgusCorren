from .piece import Piece

class Pawn(Piece):
    def __init__(self, color, position):
        self.__color__ = color
        self.__position__ = position

    def __str__(self):
        return "♙" if self.__color__ == "white" else "♟"
    
    def check_move(self, positions, new_position):

        x, y, current_x, current_y = self.get_coordinates(new_position)

        result = False

        if self.__color__ == "white":
        # Movimiento hacia adelante
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
            
        elif self.__color__ == "black":
            # Movimiento hacia adelante
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