#Importar Excepciones
from exceptions import PieceNotFoundError, InvalidMoveError

#Importar Piezas
from pieces.bishop import Bishop
from pieces.king import King
from pieces.knight import Knight
from pieces.pawn import Pawn
from pieces.queen import Queen
from pieces.rook import Rook

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

    def get_piece(self, row, col):
        return self.__positions__[row][col]
    
    def find_piece(self, piece):
        for row in range(8):
            for col in range(8):
                if self.__positions__[row][col] == piece:
                    return (row, col)
        return None

    def move(self, origen, destino):

        pos_origen = self.find_piece(origen)
        if pos_origen is None:
            raise PieceNotFoundError("La pieza de origen no se encuentra en el tablero.")
        
        if destino != object:
            origen.check_move(destino)
            
            self.__positions__[destino[0]][destino[1]] = origen
            self.__positions__[origen[0]][origen[1]] = None
            origen.set_position(destino)
        else:
            pos_destino = self.find_piece(destino)
            if pos_destino:
                if origen.get_color() == destino.get_color():
                    raise InvalidMoveError("No puedes mover donde tienes otra pieza.")
            
            origen.check_move(destino)
            
            self.__positions__[destino[0]][destino[1]] = origen
            self.__positions__[origen[0]][origen[1]] = None
            origen.set_position(destino)