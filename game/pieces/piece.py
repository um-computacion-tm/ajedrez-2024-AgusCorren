class Piece:
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
        return " "
    
    def check_move(self, positions, new_position):
        return True
    
    def get_coordinates(self, new_position):
        x, y = new_position
        current_x, current_y = self.__position__
        return x, y, current_x, current_y
    
    def diagonal_move(self, positions, new_position): # Para el alfil y la dama

        x, y, current_x, current_y = self.get_coordinates(new_position)
        x_dir, y_dir = ((x - current_x), (y - current_y))

        if abs(x_dir) == abs(y_dir):
            step_x = 1 if x_dir > 0 else -1
            step_y = 1 if y_dir > 0 else -1
            for i in range(1, abs(x_dir)):
                if positions[current_x + i * step_x][current_y + i * step_y] is not None:
                    return False
            return True

    def horizontal_move(self, positions, new_position): # Para la torre y la dama

        x, y, current_x, current_y = self.get_coordinates(new_position)

        if x == current_x and y != current_y:
            step = 1 if y > current_y else -1
            for i in range(1, abs(y - current_y)):
                if positions[x][current_y + i * step] is not None:
                    return False
            return True
    
    def vertical_move(self, positions, new_position): # Para la torre y la dama

        x, y, current_x, current_y = self.get_coordinates(new_position)

        if x != current_x and y == current_y:
            step = 1 if x > current_x else -1
            for i in range(1, abs(x - current_x)):
                if positions[current_x + i * step][current_y] is not None:
                    return False
            return True