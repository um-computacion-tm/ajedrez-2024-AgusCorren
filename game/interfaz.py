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

            selection = input("Type your selection here: ") # Pedir la selección del usuario
            print("\n")
            option = self.validate_option("start_game", selection) # Validar la selección del usuario

            if option == "Invalid option": # Si la selección es inválida, volver a pedir
                print("\n" + option + "\n")
                continue

            elif option == "Game Over": # Si la opción es "Game Over", salir del juego
                print("\n" + option + "\n")
                break

            elif option == "Game Started": # Si la opción es "Game Started", iniciar el juego
                self.__chess__ = Chess()
                self.clear_terminal()
                if self.start_game():
                    break
    
    def validate_option(self, type, option):
        result = ""
        if type == "start_game": # 
        ## Validar opciones del menú principal
            if option not in ["1", "2"]:
                result = "Invalid option"
            elif option == "2":
                result = "Game Over"
            elif option == "1":
                result = "Game Started"
            
        elif type == "continue_game":
        ## Validar opciones del menú de turno
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
            if not self.turn_menu(): # Si el jugador decide no continuar, terminar el juego
                break
            self.display_board_and_turn()

            from_input, to_input = self.get_move_input() # Obtiene la posición de origen y destino
            result = self.attempt_move(from_input, to_input) # Intenta mover la pieza

            if result in ["Black wins", "White wins", "Draw"]: # Si el juego devuelva alguna de las opciones de resultado, terminar el juego
                print(f'\n{result}')
                print("\nGame Over\n")
                return False

    def display_board_and_turn(self):
        # Muestra a quien le toca mover y le muestra el tablero
        self.clear_terminal()
        print(f"\n  {self.__chess__.turn()} TO MOVE\n")
        self.__chess__.print_board()

    def get_move_input(self):
        # Pedir al usuario la posición de origen y destino
        print('\nEnter your move')
        from_input = input('From: ')
        to_input = input('To: ')
        print('\n')
        return from_input, to_input

    def attempt_move(self, from_input, to_input, test_mode=False):
        # Intenta mover la pieza
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
        # Este Menu permite al jugador decidir si quiere continuar o no

        while True:
            self.display_turn_menu()
            selection = input("\nType your selection here: ") # Pedir la selección del usuario
            option = self.validate_option("continue_game", selection) # Validar la selección del usuario

            if option == "Invalid option":
                self.handle_invalid_option(selection) # Si la selección es inválida, mostrar la opción inválida y volver a pedir
            elif option == "Resign":
                if self.handle_resignation(): # Si la opción es "Resign", terminar el juego
                    break
            elif option == "Draw": 
                if self.handle_draw(): # Si la opción es "Draw", pedir si quiere aceptar el empate
                    break
            elif option == "Move piece": # Si la opción es "Move piece", continuar con el juego
                return True
        return False

    def display_turn_menu(self):
        # Esto es lo que el menu de turno muestra
        print('\n')
        self.__chess__.print_board()
        print('\n')
        print(f"Turn: {self.__chess__.turn()}")
        print('\nSelect an Option')
        print('1. Move piece')
        print('2. Draw')
        print('3. Resign')

    def handle_invalid_option(self, selection):
        # Esto es lo que se muestra cuando la opción seleccionada es inválida
        self.clear_terminal()
        print("\n" + f'{selection} is an invalid option, try again' + "\n")

    def handle_resignation(self):
        # Esto es lo que se muestra cuando el jugador decide resignar
        player = self.__chess__.turn()
        print(f"\n{player} resigns the game")
        winner = "BLACK" if player == "WHITE" else "WHITE"
        print(f"\n{winner} WINS")
        return True

    def handle_draw(self):
        if self.draw(self.__chess__.turn()): # Si el jugador oponente decide empatar, se muestra el mensaje de empate
            print("\nGame Drawn")
            return True
        else:
            # Si el jugador oponente no decide empatar, se muestra el mensaje de rechazo del empate
            rejecting_player = "BLACK" if self.__chess__.turn() == "WHITE" else "WHITE"
            print(f"\n{rejecting_player} REJECTS THE DRAW")
            return False
    
    def draw(self, player):
        # Opciones para cuando el jugador pide empate
        print('\n------------------------------')
        print(f"\n{player} wants to draw the game")
        print(f"\n{self.__chess__.next_turn()}, Do you want to accept the draw? [Y/N]")
        
        while True:

            option = input("Type your answer here: ") # Le piede al oponente si quiere aceptar el empate

            if option.lower() == "y":
                return True
            elif option.lower() == "n":
                return False
            else:
                print("\nInvalid input. Please enter y or n.")

    def clear_terminal(self):
        # Limpia la terminal
        os.system('cls' if os.name == 'nt' else 'clear')