from game.board import Board
from game.exceptions import PieceNotFoundError, InvalidMoveError, InvalidPosition, ChessError  
class Chess:
    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "WHITE"

    def move(self, from_row, from_col, to_row, to_col):
        try:
            # Validar coordenadas
            self.validate_cords(from_row, from_col)
            self.validate_cords(to_row, to_col)

            # Verificar y obtener pieza
            origen = self.is_a_piece(from_row, from_col)
            destino = (to_row, to_col)
            
            # Mover pieza y verificar si fue exitoso
            if self.__board__.move(origen, destino):
                self.change_turn()
                return True
            else:
                raise ChessError("Invalid move")
        except InvalidPosition as e:
            raise
        except PieceNotFoundError as e:
            raise
        except InvalidMoveError as e:
            raise
        except Exception as e:
            raise
        
        return False

    def is_a_piece(self, x, y):
        try:
            piece = self.__board__.get_piece(x, y)
            if piece is None:
                raise PieceNotFoundError(f'In {(x, y)} position there is no piece')
            return piece
        except PieceNotFoundError as e:
            print(f"Error: {e}")
            raise
    
    def validate_cords (self, x, y):
        if (0<= x < 8 and 0<= y < 8):
            return True
        else:
            raise InvalidPosition("Invalid position, must be between 0 and 7")

    def turn(self):
        return self.__turn__
    
    def change_turn(self):
        if self.__turn__ == "WHITE":
            self.__turn__ = "BLACK"
        else:
            self.__turn__ = "WHITE"
    
    def print_board(self):
        self.__board__.print_board()