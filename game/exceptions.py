class ChessError(Exception):
    pass

class PieceNotFoundError(ChessError):
    "Excepcion cuando no se encuentra una pieza en el tablero"
    def __init__(self, message="Piece not found."):
        self.message = message
        super().__init__(self.message)

class InvalidMoveError(ChessError):
    "Excepcion para movimientos invalidos"
    def __init__(self, message="Invalid Move"):
        self.message = message
        super().__init__(self.message)

class InvalidPosition(ChessError):
    "Excepcion para posiciones invalidas"
    def __init__(self, message="Invalid Position"):
        self.message = message
        super().__init__(self.message)

class ColorError(ChessError):
    "Excepcion para posiciones piezas de color diferente"
    def __init__(self, message="Cannot move a piece of a different color"):
        self.message = message

class InvalidPieceMovement(InvalidMoveError):
    "Excepcion para movimientos invalidos"
    def __init__(self, message="Invalid Piece Movement"):
        self.message = message
        super().__init__(self.message)

class CantEatKing(ChessError):
    "Excepcion para que no se pueda comer un rey"
    def __init__(self, message="You can't eat a king"):
        self.message = message
        super().__init__(self.message)