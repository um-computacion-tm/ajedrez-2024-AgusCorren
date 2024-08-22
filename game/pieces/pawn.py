from .piece import Piece

class Pawn(Piece):
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
        return "♙" if self.__color__ == "white" else "♟"
    
    def check_move(self, positions, new_position):
        x, y = new_position
        current_x, current_y = self.__position__

        if self.__color__ == "white":
        # Movimiento hacia adelante
            if y == current_y:
                if current_x == 6:
                    if x == current_x - 1 and positions[current_x - 1][current_y] is None:
                        return True
                    elif x == current_x - 2 and positions[current_x - 1][current_y] is None and positions[current_x - 2][current_y] is None:
                        return True
                elif x == current_x - 1 and positions[current_x - 1][current_y] is None:
                    return True
            # Movimiento de captura
            elif x == current_x - 1 and abs(y - current_y) == 1 and positions[x][y] is not None:
                return True
            
        elif self.__color__ == "black":
            # Movimiento hacia adelante
            if y == current_y:
                if current_x == 1:
                    if x == current_x + 1 and positions[current_x + 1][current_y] is None:
                        return True
                    elif x == current_x + 2 and positions[current_x + 1][current_y] is None and positions[current_x + 2][current_y] is None:
                        return True
                elif x == current_x + 1 and positions[current_x + 1][current_y] is None:
                    return True
            # Movimiento de captura
            elif x == current_x + 1 and abs(y - current_y) == 1 and positions[x][y] is not None:
                return True

        return False