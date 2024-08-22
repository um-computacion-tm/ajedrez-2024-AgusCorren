#Importar Excepciones
from game.exceptions import PieceNotFoundError, InvalidMoveError, InvalidPieceMovement

#Importar Piezas
from game.pieces.piece import Piece
from game.pieces.bishop import Bishop
from game.pieces.king import King
from game.pieces.knight import Knight
from game.pieces.pawn import Pawn
from game.pieces.queen import Queen
from game.pieces.rook import Rook

class Board:
    def __init__(self):
        # Crea una matriz vacia de 8x8 (TABLERO)
        self.__positions__ = []
        for _ in range(8):
            col = []
            for _ in range(8):
                col.append(None)
            self.__positions__.append(col)

        self.setup_pieces()

    def setup_pieces(self):
        self.__positions__[0][0] = Rook("black",(0,0))
        self.__positions__[0][1] = Knight("black",(0,1))
        self.__positions__[0][2] = Bishop("black",(0,2))
        self.__positions__[0][3] = Queen("black",(0,3))
        self.__positions__[0][4] = King("black",(0,4))
        self.__positions__[0][5] = Bishop("black",(0,5))
        self.__positions__[0][6] = Knight("black",(0,6))
        self.__positions__[0][7] = Rook("black",(0,7))

        for i in range(8): # Rellena las filas indicadas de Peones  (1 y 6)
            self.__positions__[1][i]= Pawn("black",(1,i))
            self.__positions__[6][i]= Pawn("white",(6,i))

        self.__positions__[7][0] = Rook("white",(7,0))
        self.__positions__[7][1] = Knight("white",(7,1))
        self.__positions__[7][2] = Bishop("white",(7,2))
        self.__positions__[7][3] = Queen("white",(7,3))
        self.__positions__[7][4] = King("white",(7,4))
        self.__positions__[7][5] = Bishop("white",(7,5))
        self.__positions__[7][6] = Knight("white",(7,6))
        self.__positions__[7][7] = Rook("white",(7,7))

    def get_piece(self, row, col): # Devuelve la pieza en la posicion indicada
        return self.__positions__[row][col]
    
    def find_piece(self, piece): # Devuelve la posicion de la pieza encontrada
        if piece is not None:
            for row in range(8):
                for col in range(8):
                    if self.__positions__[row][col] == piece:
                        return (row, col)
            return None
        else:
            return None

    def move(self, origen, destino):
        try:
            self.validate_move(origen, destino)
            self.execute_move(origen, destino)
            return True
        except PieceNotFoundError as e:
            raise
        except InvalidPieceMovement as e:
            print(f"Error: {e}")
            raise

        except InvalidMoveError as e:
            print(f"Error: {e}")
            raise  

        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            raise

    def validate_move(self, origen, destino):
        pos_origen = self.find_piece(origen)
        destino_piece = self.get_piece(destino[0], destino[1])
        
        if origen is None:
            raise PieceNotFoundError("Piece not found on the board.")
        
        elif pos_origen is None:
            raise PieceNotFoundError("Piece not found on the board.")
        
        # Validar si el tipo de movimiento de la pieza es valido
        elif origen.check_move(self.__positions__,destino) == False:
            raise InvalidPieceMovement("Invalid Piece Movement, try again")

        if isinstance(destino_piece, Piece):
            if origen.get_color() == destino_piece.get_color():
                raise InvalidMoveError("You cannot move where you have another piece.")

    def execute_move(self, origen, destino):
        pos_origen = self.find_piece(origen)
        pos_destino = destino
        destino = self.get_piece(destino[0], destino[1])

        self.__positions__[pos_destino[0]][pos_destino[1]] = origen
        self.__positions__[pos_origen[0]][pos_origen[1]] = None
        origen.set_position(pos_destino)
        if destino is not None:
            destino.set_position(None)

    def print_board(self):
        # Imprime el tablero de ajedrez
        for row in range(7, -1, -1):
            line = ''
            for col in range(8):
                piece = self.get_piece(row, col)
                if piece is None:
                    line += '. '  
                else:
                    line += f'{piece} '
            print(line)
    
    def color_pieces(self, x, y):
        piece = self.get_piece(x, y)
        if piece is None:
            raise PieceNotFoundError("Piece not found on the board.")
        else:
            return piece.get_color()