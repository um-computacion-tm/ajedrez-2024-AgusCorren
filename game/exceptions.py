class ChessError(Exception):
    """Clase base para las excepciones de ajedrez."""
    def __init__(self, message="An error occurred in the chess game."):
        self.message = message
        super().__init__(self.message)

class PieceNotFoundError(ChessError):
    """Excepción cuando no se encuentra una pieza en el tablero."""
    def __init__(self, message="Piece not found."):
        super().__init__(message)

class InvalidMoveError(ChessError):
    """Excepción para movimientos inválidos."""
    def __init__(self, message="Invalid Move"):
        super().__init__(message)

class InvalidPosition(ChessError):
    """Excepción para posiciones inválidas."""
    def __init__(self, message="Invalid Position"):
        super().__init__(message)

class ColorError(ChessError):
    """Excepción para mover piezas de un color diferente."""
    def __init__(self, message="Cannot move a piece of a different color"):
        super().__init__(message)

class InvalidPieceMovement(InvalidMoveError):
    """Excepción para movimientos inválidos de una pieza."""
    def __init__(self, message="Invalid Piece Movement"):
        super().__init__(message)