from .piece import Piece

class Bishop(Piece):
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
        return "♗" if self.__color__ == "white" else "♝"
    
    def check_move(self, positions, new_position):
        x, y = new_position
        current_x, current_y = self.__position__
        x_dir, y_dir = ((x - current_x), (y - current_y))

        if abs(x_dir) == abs(y_dir):
            step_x = 1 if x_dir > 0 else -1
            step_y = 1 if y_dir > 0 else -1
            for i in range(1, abs(x_dir)):
                if positions[current_x + i * step_x][current_y + i * step_y] is not None:
                    return False
            return True

        return False
    

