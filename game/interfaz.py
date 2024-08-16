from game.chess_game import Chess
from game.exceptions import PieceNotFoundError, InvalidMoveError, InvalidPosition

class Interfaz:
    def __init__(self):
        self.__chess__ = Chess()

    def menu(self):
        while True:
            print('\nChessGame - By Agustin Correnti')
            print('------------------------------\n')
            print('Select an Option')
            print('1. Start Game')
            print('2. Exit\n')

            selection = input("Type your selection here: ")
            option = self.validate_option(selection)

            if option == "Invalid option":
                print("\n" + option + "\n")
                continue

            elif option == "Game Over":
                print("\n" + option + "\n")
                break

            elif option == "Game Started":
                self.start_game()
    
    def validate_option(self, option):
        if option not in "12":
            return "Invalid option"
        elif option == "2":
            return "Game Over"
        elif option == "1":
            return "Game Started"
    
    def start_game(self):
        while True:
            print("\nTurn: ", self.__chess__.turn(), "TO MOVE\n")
            self.__chess__.print_board()
            print('\nSelect an Option')

            try:
                from_row = int(input('From row: '))
                from_col = int(input('From column: '))
                to_row = int(input('To row: '))
                to_col = int(input('To column: '))

                print('\n')
                
                # Intentar mover la pieza y cambiar de turno solo si el movimiento fue exitoso
                self.__chess__.move(from_row, from_col, to_row, to_col)

            except ValueError:
                print("Invalid input! Please enter numbers between 0 and 7 for rows and columns.")