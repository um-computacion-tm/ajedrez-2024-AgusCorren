from board import Board
from exceptions import PieceNotFoundError, InvalidMoveError, InvalidPosition
class Chess:
    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "WHITE"

    def move(self, from_row, from_col, to_row, to_col):
        # Validate Coords
        if (0<= from_row < 8 and 0<= from_col < 8 and 0<= to_row < 8 and 0<= to_col < 8):

            origen = self.__board__.get_piece(from_row, from_col)
            destino = self.__board__.get_piece(to_row, to_col)
            
            self.__board__.move(origen, destino)
            self.change_turn()
        else:
            raise InvalidPosition("La posición de destino está fuera del tablero.")

    def turn(self):
        return self.__turn__
    
    def change_turn(self):
        if self.__turn__ == "WHITE":
            self.__turn__ = "BLACK"
        else:
            self.__turn__ = "WHITE"