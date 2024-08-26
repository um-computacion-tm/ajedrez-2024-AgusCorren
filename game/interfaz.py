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
                self.clear_terminal()
                self.start_game()
                break
    
    def validate_option(self, type, option):
        if type == "start_game":
        ## Validar opciones de menu
                    if option not in "12":
                        return "Invalid option"
                    elif option == "2":
                        return "Game Over"
                    elif option == "1":
                        return "Game Started"
        
        elif type == "continue_game":
        ## Validar opciones de menu
            if option not in "123":
                return "Invalid option"
            elif option == "3":
                return "Resign"
            elif option == "2":
                return "Draw"
            elif option == "1":
                return "Move piece"

    
    def start_game(self):
        while True:
            ## Imprimer el tablero y el turno
            if not self.turn_menu():
                break
            print("\n")
            self.clear_terminal()
            print(f"\n  {self.__chess__.turn()} TO MOVE\n")
            self.__chess__.print_board()

            print('\nEnter your move')
            from_input = input('From: ')
            to_input = input('To: ')
            print('\n')

            try:
                self.clear_terminal()
                print('\n')
                if self.__chess__.move(from_input, to_input):
                    continue
                else:
                    print(self.__chess__.move(from_input, to_input))
                
            except ValueError as e:
                print(e)
                continue
            except PieceNotFoundError as e:
                continue
            except InvalidPieceMovement as e:
                continue
            except InvalidMoveError as e:
                continue
            except InvalidPosition as e:
                continue
            except ColorError as e:
                continue
            except ChessError as e:
                continue
            except Exception as e:
                continue

    def turn_menu(self):
        ## Este Menu permite al jugador decidir si quiere continuar o no

        while True:
            print('\n')
            self.__chess__.print_board()
            print('\n')
            print("Turn: ", self.__chess__.turn())
            print('\nSelect an Option')
            print('1. Move piece')
            print('2. Draw')
            print('3. Resign')
            selection = input("\nType your selection here: ")
            option = self.validate_option("continue_game", selection)

            if option == "Invalid option":
                self.clear_terminal()
                print("\n" + f'{selection} is a Invalid option, try again' + "\n")
                continue
            elif option == "Resign":
                player = self.__chess__.turn()
                print(f"\n{player} resigns the game")
                if player == "WHITE":
                    print(f"\nBLACK WINS")
                    break
                elif player == "BLACK":
                    print(f"\nWHITE WINS")
                    break
            elif option == "Draw":
                if self.draw(self.__chess__.turn()):
                    print("\nGame Drawn")
                    break
                else:
                    if self.__chess__.turn() == "WHITE":
                        print(f"\nBLACK REJECTS THE DRAW")
                        continue
                    elif self.__chess__.turn():
                        print(f"\nWHITE REJECTS THE DRAW")
                        continue
            elif option == "Move piece":
                return True
        return False
    
    def draw(self, player):

        print('\n------------------------------')
        print(f"\n{player} wants to draw the game")
        self.__chess__.change_turn()
        print(f"\n{self.__chess__.turn()}, Do you want to accept the draw? [Y/N]")
        
        while True:
            try:
                option = input("Type your answer here: ")
                if option.lower() == "y":
                    return True
                elif option.lower() == "n":
                    self.__chess__.change_turn()
                    break
            except ValueError:
                print("\nInvalid input. Please enter numeric values.")

        return False

    def clear_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')