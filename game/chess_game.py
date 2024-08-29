from game.board import Board
from game.exceptions import PieceNotFoundError, InvalidMoveError, InvalidPosition, InvalidPieceMovement, ColorError, ChessError  
class Chess:
    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "WHITE"

    def move(self, from_input, to_input):
        try:
            # Validar coordenadas
            x, y = self.translate_input(from_input)
            x1, y1 = self.translate_input(to_input)

            # Verificar si es una pieza y si es del mismo color que turno
            origen = self.own_pieces(x, y)

            destino = (x1, y1)
            
            # Mover pieza y verificar si fue exitoso
            mover_pieza = self.__board__.move(origen, destino)
            status = self.check_victory()

            if mover_pieza:
                if status == "Draw":
                    return "Draw"
                elif status == "Black wins":
                    return "Black wins"
                elif status == "White wins":
                    return "White wins"
                else:
                    self.change_turn()  # Cambiar turno si el juego continúa
                    return True  # Movimiento válido pero el juego no ha terminado

            
        except InvalidPosition as e:
            print(f"Error: {e}")
            raise

        except PieceNotFoundError as e:
            print(f"Error: {e}")
            raise

        except InvalidPieceMovement as e:
            raise
        
        except ValueError:
            raise

        except ColorError as e:
            print(f"Error: {e}")
            raise


    def turn(self):
        return self.__turn__
    
    def change_turn(self):
        if self.__turn__ == "WHITE":
            self.__turn__ = "BLACK"
        else:
            self.__turn__ = "WHITE"
    
    def print_board(self):
        self.__board__.print_board()

    def own_pieces(self, x, y):
        try:
            piece = self.__board__.get_piece(x, y)
            if piece is None:
                raise PieceNotFoundError(f'In {(x, y)} position there is no piece')

            color_turn = self.__turn__.lower()
            color_piece = self.__board__.color_pieces(x, y).lower()

            if color_turn == color_piece:
                return piece
            else:
                raise ColorError("Cannot move a piece of a different color")
            
        except PieceNotFoundError as e:
            raise
    
    def check_victory(self):

        pieces_alive = self.__board__.pieces_on_board()

        if pieces_alive[0] > 1 and pieces_alive[1] < 2 and self.__turn__ == "BLACK":
        # Si el rey blanco tiene una pieza de mas y el rey negro esta solo y es su turno, entonces el rey blanco gana
            return "White wins"
        elif pieces_alive[1] > 1 and pieces_alive[0] < 2 and self.__turn__ == "WHITE":
        # Si el rey negro tiene una pieza de mas y el rey blanco esta solo y es su turno, entonces el rey negro gana
            return "Black wins"
        elif pieces_alive[0] + pieces_alive[1] == 2:
        # Si quedan los dos reyes solos, entonces el juego termina en empate
            return "Draw"
        return True

    def translate_input(self, input_str):
        """
        Transforma una entrada de tipo 'A2' a coordenadas (fila, columna).
        """
        # Asegurarse de que la entrada tenga dos caracteres
        if len(input_str) != 2:
            raise ValueError("Input must be 2 characters long, like 'A2'.")

        # Diccionario de mapeo de letras a números de columnas
        letter_to_col = {
            'A': 0, 'B': 1, 'C': 2, 'D': 3,
            'E': 4, 'F': 5, 'G': 6, 'H': 7
        }
        
        # Obtener la letra y el número de la entrada
        letter = input_str[0].upper()
        num = input_str[1]
        
        # Convertir la letra a un índice de columna
        if letter not in letter_to_col:
            raise InvalidPosition(f"[{input_str[0]}] from [{input_str}], must be a letter from A to H.")
        col = letter_to_col[letter]

        # Convertir el número de la columna
        try:

            row = int(num)
            if row < 0 or row > 7:
                raise InvalidPosition(f"Second character from [{input_str}], must be a number from 1 to 8.")
            return (row, col)
        
        except ValueError:
            raise ValueError(f"Second character from [{input_str}], must be a number.")
        except InvalidPosition:
            raise        