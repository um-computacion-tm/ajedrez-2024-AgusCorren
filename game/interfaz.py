from game.chess_game import Chess
from game.exceptions import *
import os

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
            print("\n")
            option = self.validate_option("start_game", selection)

            if option == "Invalid option":
                print("\n" + option + "\n")
                continue

            elif option == "Game Over":
                print("\n" + option + "\n")
                break

            elif option == "Game Started":
                self.__chess__ = Chess()
                self.clear_terminal()
                if self.start_game():
                    break
    
    def validate_option(self, type, option):
        result = ""
        if type == "start_game":
        ## Validar opciones de menu
            if option not in ["1", "2"]:
                result = "Invalid option"
            elif option == "2":
                result = "Game Over"
            elif option == "1":
                result = "Game Started"
            
        elif type == "continue_game":
        ## Validar opciones de menu
            if option not in ["1", "2", "3"]:
                result = "Invalid option"
            elif option == "3":
                result = "Resign"
            elif option == "2":
                result = "Draw"
            elif option == "1":
                result = "Move piece"

        return result

    
    def start_game(self):
        while True:
            if not self.turn_menu():
                break
            self.display_board_and_turn()

            from_input, to_input = self.get_move_input()
            result = self.attempt_move(from_input, to_input)

            if result in ["Black wins", "White wins", "Draw"]:
                print(f'\n{result}')
                print("\nGame Over\n")
                return False

    def display_board_and_turn(self):
        self.clear_terminal()
        print(f"\n  {self.__chess__.turn()} TO MOVE\n")
        self.__chess__.print_board()

    def get_move_input(self):
        print('\nEnter your move')
        from_input = input('From: ')
        to_input = input('To: ')
        print('\n')
        return from_input, to_input

    def attempt_move(self, from_input, to_input, test_mode=False):
        try:
            self.clear_terminal()
            print('\n')
            result = self.__chess__.move(from_input, to_input)
            return result
        except (ValueError, CantEatKingError, PieceNotFoundError, InvalidPieceMovement, InvalidMoveError, InvalidPosition, ColorError, ChessError) as e:
            if test_mode:
                raise
            print(e)
        except Exception as e:
            if test_mode:
                raise

    def turn_menu(self):
        ## Este Menu permite al jugador decidir si quiere continuar o no

        while True:
            self.display_turn_menu()
            selection = input("\nType your selection here: ")
            option = self.validate_option("continue_game", selection)

            if option == "Invalid option":
                self.handle_invalid_option(selection)
            elif option == "Resign":
                if self.handle_resignation():
                    break
            elif option == "Draw":
                if self.handle_draw():
                    break
            elif option == "Move piece":
                return True
        return False

    def display_turn_menu(self):
        print('\n')
        self.__chess__.print_board()
        print('\n')
        print(f"Turn: {self.__chess__.turn()}")
        print('\nSelect an Option')
        print('1. Move piece')
        print('2. Draw')
        print('3. Resign')

    def handle_invalid_option(self, selection):
        self.clear_terminal()
        print("\n" + f'{selection} is an invalid option, try again' + "\n")

    def handle_resignation(self):
        player = self.__chess__.turn()
        print(f"\n{player} resigns the game")
        winner = "BLACK" if player == "WHITE" else "WHITE"
        print(f"\n{winner} WINS")
        return True

    def handle_draw(self):
        if self.draw(self.__chess__.turn()):
            print("\nGame Drawn")
            return True
        else:
            rejecting_player = "BLACK" if self.__chess__.turn() == "WHITE" else "WHITE"
            print(f"\n{rejecting_player} REJECTS THE DRAW")
            return False
    
    def draw(self, player):

        print('\n------------------------------')
        print(f"\n{player} wants to draw the game")
        self.__chess__.change_turn()
        print(f"\n{self.__chess__.turn()}, Do you want to accept the draw? [Y/N]")
        
        while True:

            option = input("Type your answer here: ")  

            if option.lower() == "y":
                return True
            elif option.lower() == "n":
                self.__chess__.change_turn()
                return False
            else:
                print("\nInvalid input. Please enter y or n.")

    def clear_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')