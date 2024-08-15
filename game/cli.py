from chess import Chess
from exceptions import PieceNotFoundError, InvalidMoveError, InvalidPosition

def main():
    chess = Chess()
    while True:
        play(chess)

def play(chess):

     try:
          print("turn: ", chess.turn(), "TO MOVE")
          from_row = int(input('From row: '))
          from_col = int(input('From column: '))
          to_row = int(input('To row: '))
          to_col = int(input('To column: '))

          chess.move(from_row, from_col, to_row, to_col)
     except PieceNotFoundError as e:
          print(e)
     except InvalidMoveError as e:
          print(e)
     except InvalidPosition as e:
          print(e)
     except Exception as e:
          print("Error inesperado:", e)
         

if __name__ == '__main__':
    main()