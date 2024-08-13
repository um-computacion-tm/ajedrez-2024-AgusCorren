from pieces.bishop import Bishop
from pieces.king import King
from pieces.knight import Knight
from pieces.pawn import Pawn
from pieces.queen import Queen
from pieces.rook import Rook

class Board:
    def __init__(self):
        self.__positions__ = []
        for _ in range(8): # Crea la matriz del tablero
            col = []
            for _ in range(8):
                col.append(None)
            self.positions.append(col)
        self.__positions__[0][0] = Rook("black")
        self.__positions__[0][1] = Knight("black")
        self.__positions__[0][2] = Bishop("black")
        self.__positions__[0][3] = Queen("black")
        self.__positions__[0][4] = King("black")
        self.__positions__[0][5] = Bishop("black")
        self.__positions__[0][6] = Knight("black")
        self.__positions__[0][7] = Rook("black")
        for i in range(8): # Rellena de Peones en las filas indicadas (1 y 6)
            self.__positions__[1][i]= Pawn("black")
            self.__positions__[6][i]= Pawn("white")
        self.__positions__[7][0] = Rook("white")
        self.__positions__[7][1] = Knight("white")
        self.__positions__[7][2] = Bishop("white")
        self.__positions__[7][3] = Queen("white")
        self.__positions__[7][4] = King("white")
        self.__positions__[7][5] = Bishop("white")
        self.__positions__[7][6] = Knight("white")
        self.__positions__[7][7] = Rook("white") 

            
    def get_piece(self, row, col):
        return self.__positions__[row][col]