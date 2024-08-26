from .piece import Piece

class Pawn(Piece):
    def __init__(self, color, position):
        self.__color__ = color
        self.__position__ = position

    def __str__(self):
        return "♙" if self.__color__ == "white" else "♟"
    
    def check_move(self, positions, new_position):
        if self.__color__ == "white":
            return self.is_valid_white_move(positions, new_position)
        elif self.__color__ == "black":
            return self.is_valid_black_move(positions, new_position)
        return False

    def is_valid_white_move(self, positions, new_position):
        ## Valida si el tipo de movimiento del peon blanco, envia la direccion y la fila inicial
        return self.is_valid_pawn_move(positions, new_position, -1, 6)

    def is_valid_black_move(self, positions, new_position):
        ## Valida si el tipo de movimiento del peon negro, envia la direccion y la fila inicial
        return self.is_valid_pawn_move(positions, new_position, 1, 1)

    def is_valid_pawn_move(self, positions, new_position, direction, initial_row):
        x, y, current_x, current_y = self.get_coordinates(new_position)
        result = False

        if y == current_y: # Valida que el movimiento sea en la misma columna
            if current_x == initial_row:
                if self.move_one_cell(positions, new_position, direction):
                    result = True
                elif x == current_x + 2 * direction and positions[current_x + direction][current_y] is None and positions[current_x + 2 * direction][current_y] is None:
                    result = True
            elif self.move_one_cell(positions, new_position, direction):
                result = True
        elif x == current_x + direction and abs(y - current_y) == 1 and positions[x][y] is not None:
        # Movimiento de captura
            result = True
        return result
    
    def move_one_cell(self, positions, new_position, direction):
        x, y, current_x, current_y = self.get_coordinates(new_position)
        if x == current_x + direction and positions[current_x + direction][current_y] is None:
            return True
        return False
    
    