class ChessError(Exception):
    pass

class PieceNotFoundError(ChessError):
    "Excepcion cuando no se encuentra una pieza en el tablero"
    def __init__(self, message="La pieza no se encuentra en el tablero"):
        self.message = message
        super().__init__(self.message)

class InvalidMoveError(ChessError):
    "Excepcion para movimientos invalidos"
    def __init__(self, message="Movimiento inválido"):
        self.message = message
        super().__init__(self.message)

class InvalidPosition(ChessError):
    "Excepcion para posiciones invalidas"
    def __init__(self, message="Posicion Invalida"):
        self.message = message
        super().__init__(self.message)