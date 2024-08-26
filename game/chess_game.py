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

            '''
            El check_victory() aun no esta completo del todo
            '''

            if mover_pieza and status:
                self.change_turn()
                return True
            elif status == "Black wins":
                return "Black wins"
            elif status == "White wins":
                return "White wins"
            elif status == "Draw":
                return "Draw"
            
        except InvalidPosition as e:
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

        if pieces_alive[0] > 1 and pieces_alive[1] < 2:
            return "White wins"
        elif pieces_alive[1] > 1 and pieces_alive[0] < 2:
            return "Black wins"
        elif pieces_alive[0] + pieces_alive[1] == 2:
            return "Draw"
        else:
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
            raise ValueError("First character must be a letter from A to H.")
        col = letter_to_col[letter]

        # Convertir el número de la columna
        try:

            row = int(num)
            if row < 0 or row > 7:
                raise ValueError("Second character must be a number from 1 to 8.")
            return (row, col)
        
        except ValueError:
            raise ValueError("Second character must be a number.")
        except InvalidPosition:
            raise        