from .piece import Piece

class Queen(Piece):
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
        return "♕" if self.__color__ == "white" else "♛"
    
    def check_move(self, positions, new_position):
        x, y = new_position
        current_x, current_y = self.__position__
        x_dir, y_dir = ((x - current_x), (y - current_y))

        if abs(x_dir) == abs(y_dir):
            # Movimiento diagonal
            step_x = 1 if x_dir > 0 else -1
            step_y = 1 if y_dir > 0 else -1
            for i in range(1, abs(x_dir)):
                if positions[current_x + i * step_x][current_y + i * step_y] is not None:
                    return False
            return True
                
        elif x == current_x and y != current_y:
            # Movimiento Horizontal
            for i in range(1, abs(y - current_y)):
                if y > current_y:  # Movimiento hacia la derecha
                    if positions[x][current_y + i] is not None:
                        return False
                else:  # Movimiento hacia la izquierda
                    if positions[x][current_y - i] is not None:
                        return False
            return True
        elif x != current_x and y == current_y:
            # Movimiento Vertical
            for i in range(1, abs(x - current_x)):
                if x > current_x:  # Movimiento hacia arriba
                    if positions[current_x + i][current_y] is not None:
                        return False
                else:  # Movimiento hacia abajo
                    if positions[current_x - i][current_y] is not None:
                        return False
            return True
        return False