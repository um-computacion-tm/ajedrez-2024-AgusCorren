import unittest
from unittest.mock import patch, MagicMock
from game.interfaz import Interfaz
from game.chess_game import Chess
from game.exceptions import *

class TestInterfaz(unittest.TestCase):
    def setUp(self):
        self.__interfaz__ = Interfaz()

    @patch('builtins.input', side_effect=['1', '2'])
    @patch('game.interfaz.Interfaz.start_game')
    def test_menu_valid_options(self, mock_start_game, mock_input):
        self.__interfaz__.menu()
        mock_start_game.assert_called_once()
        with patch('builtins.print') as mock_print:
            self.__interfaz__.menu()
            mock_print.assert_called_with("\nGame Over\n")

    @patch('builtins.input', side_effect=['y'])  # Simula la entrada para aceptar el empate
    @patch('game.interfaz.Interfaz.draw')  # Mockea draw
    def test_handle_draw(self, mock_draw, mock_input):
        mock_draw.return_value = True  # Simula que el empate es aceptado
        
        with patch('builtins.print') as mock_print:
            result = self.__interfaz__.handle_draw()  # Ejecuta handle_draw
            self.assertTrue(result)  # Verifica que handle_draw devuelva True
            mock_print.assert_called_with("\nGame Drawn")  # Verifica que se imprime el mensaje de empate


    def test_validate_option_start_game(self):
        self.assertEqual(self.__interfaz__.validate_option("start_game", "1"), "Game Started")
        self.assertEqual(self.__interfaz__.validate_option("start_game", "2"), "Game Over")
        self.assertEqual(self.__interfaz__.validate_option("start_game", "3"), "Invalid option")

    def test_validate_option_continue_game(self):
        self.assertEqual(self.__interfaz__.validate_option("continue_game", "1"), "Move piece")
        self.assertEqual(self.__interfaz__.validate_option("continue_game", "2"), "Draw")
        self.assertEqual(self.__interfaz__.validate_option("continue_game", "3"), "Resign")
        self.assertEqual(self.__interfaz__.validate_option("continue_game", "4"), "Invalid option")

    @patch('builtins.input', side_effect=['y'])
    def test_draw_accept(self, mock_input):
        result = self.__interfaz__.draw('WHITE')
        self.assertTrue(result)

    @patch('builtins.input', side_effect=['n'])
    def test_draw_reject(self, mock_input):
        result = self.__interfaz__.draw('WHITE')
        self.assertFalse(result)
    
    @patch('game.interfaz.Chess')
    def test_handle_resignation(self, MockChess):
        mock_chess = MockChess.return_value
        mock_chess.turn.return_value = "WHITE"
        self.__interfaz__.__chess__ = mock_chess

        with patch('builtins.print') as mock_print:
            result = self.__interfaz__.handle_resignation()
            self.assertTrue(result)
            mock_print.assert_any_call("\nWHITE resigns the game")
            mock_print.assert_any_call("\nBLACK WINS")
    
    @patch('game.interfaz.Interfaz.draw')
    def test_handle_draw_reject(self, mock_draw):
        mock_draw.return_value = False
        with patch('builtins.print') as mock_print:
            result = self.__interfaz__.handle_draw()
            self.assertFalse(result)
            mock_print.assert_called_with("\nBLACK REJECTS THE DRAW")

    @patch('builtins.print')
    @patch('game.interfaz.Chess')
    @patch('builtins.input', side_effect=['1'])  # Simula la opción de mover una pieza
    def test_turn_menu_move_piece(self, mock_input, MockChess, mock_print):
        mock_chess = MockChess.return_value
        mock_chess.turn.return_value = "WHITE"
        self.__interfaz__.__chess__ = mock_chess
        self.__interfaz__.turn_menu()

        # Verifica que se imprimen los mensajes correctos
        mock_print.assert_any_call('\n')
        mock_print.assert_any_call('\nSelect an Option')
        mock_print.assert_any_call('1. Move piece')
        mock_print.assert_any_call('2. Draw')
        mock_print.assert_any_call('3. Resign')
        mock_print.assert_any_call('3. Resign')
    
    @patch('builtins.input', side_effect=['2', 'n', '3'])  # '2' para Draw y 'n' para rechazar el empate
    @patch('game.interfaz.Interfaz.draw')
    def test_turn_menu_draw_reject(self, mock_draw, mock_input):
        mock_draw.return_value = False  # Simula que el empate es rechazado
        
        with patch('builtins.print') as mock_print:
            result = self.__interfaz__.turn_menu()
            
            # El resultado debería ser False ya que el empate fue rechazado
            self.assertFalse(result)
            
            # Verifica que se imprimió el mensaje de rechazo del empate

            mock_print.assert_any_call("\nBLACK REJECTS THE DRAW")

            # Luego de que Negro rechace, Blanco se rinde y gana Negro
            mock_print.assert_any_call("\nWHITE resigns the game")
            mock_print.assert_any_call("\nBLACK WINS")
    
    @patch('builtins.input', side_effect=['2', 'y'])  # '2' para Draw y 'y' para aceptar el empate
    @patch('game.interfaz.Interfaz.draw')
    def test_turn_menu_draw_accept(self, mock_draw, mock_input):
        mock_draw.return_value = True  # Simula que el empate es aceptado

        with patch('builtins.print') as mock_print:
            result = self.__interfaz__.turn_menu()
            
            # El resultado debería ser False ya que el empate fue aceptado y se rompe el bucle
            self.assertFalse(result)

            # Verifica que los mensajes correctos fueron impresos
            mock_print.assert_any_call("Turn: WHITE")
            mock_print.assert_any_call("\nSelect an Option")
            mock_print.assert_any_call("1. Move piece")
            mock_print.assert_any_call("2. Draw")
            mock_print.assert_any_call("3. Resign")
            mock_print.assert_any_call("\nGame Drawn")




class TestInterfazMoves(unittest.TestCase):
    @patch('game.interfaz.Chess')
    def setUp(self, MockChess):
        self.mock_chess = MockChess.return_value
        self.interfaz = Interfaz()

    def test_initialization(self):
        self.assertIsInstance(self.interfaz.__chess__, MagicMock)
    
    @patch('builtins.print')
    def test_display_board_and_turn(self, mock_print):
        self.interfaz.display_board_and_turn()
        mock_print.assert_any_call(f"\n  {self.mock_chess.turn()} TO MOVE\n")
        self.mock_chess.print_board.assert_called_once()

    @patch('builtins.input', side_effect=['e2', 'e4'])
    @patch('builtins.print')
    def test_get_move_input(self, mock_print, mock_input):
        from_input, to_input = self.interfaz.get_move_input()
        self.assertEqual(from_input, 'e2')
        self.assertEqual(to_input, 'e4')

    @patch('builtins.print')
    @patch('game.interfaz.Interfaz.clear_terminal')
    def test_attempt_move(self, mock_clear_terminal, mock_print):
        self.mock_chess.move.return_value = True
        with patch('game.interfaz.Interfaz.get_move_input', return_value=('e2', 'e4')):
            self.interfaz.attempt_move('e2', 'e4', test_mode=True)
            self.assertTrue(self.mock_chess.move.called)

        # Simular diferentes excepciones
        for exception_class in [
            CantEatKingError,
            InvalidPosition,
            ColorError,
            PieceNotFoundError,
            InvalidPieceMovement,
            InvalidMoveError,
            ChessError,
            Exception
        ]:
            with self.subTest(exception=exception_class):
                self.mock_chess.move.side_effect = exception_class("Invalid move")
                with self.assertRaises(exception_class):
                    self.interfaz.attempt_move('e2', 'e4', test_mode=True)

    @patch('builtins.input', side_effect=['3', '2'])
    @patch('builtins.print')
    def test_menu_invalid_options(self, mock_print, mock_input):
        interfaz = Interfaz()
        
        interfaz.menu()

        # Verifica que se imprimió "Invalid option" cuando se seleccionó '3'
        mock_print.assert_any_call("\nInvalid option\n")
        
        # Verifica que se imprimió "Game Over" cuando se seleccionó '2'
        mock_print.assert_any_call("\nGame Over\n")

    @patch('game.interfaz.Interfaz.turn_menu', side_effect=[True, True, True])
    @patch('game.interfaz.Interfaz.display_board_and_turn')
    @patch('game.interfaz.Interfaz.get_move_input', side_effect=[('e2', 'e4'), ('a7', 'a8'), ('a8', 'a7')])
    @patch('game.interfaz.Interfaz.attempt_move', side_effect=['Continue', 'Continue', 'Black wins'])
    @patch('builtins.print')
    def test_start_game_game_over(self, mock_print, mock_attempt_move, mock_get_move_input, mock_display_board_and_turn, mock_turn_menu):
        interfaz = Interfaz()
        interfaz.start_game()

        # Verificar que turn_menu es llamado múltiples veces
        self.assertEqual(mock_turn_menu.call_count, 3)

        # Verificar que display_board_and_turn es llamado tres veces (una vez por cada turno)
        self.assertEqual(mock_display_board_and_turn.call_count, 3)

        # Verificar que get_move_input es llamado tres veces (una vez por cada movimiento)
        self.assertEqual(mock_get_move_input.call_count, 3)

        # Verificar que attempt_move es llamado tres veces (una vez por cada movimiento)
        self.assertEqual(mock_attempt_move.call_count, 3)

        # Verificar que el mensaje "Black wins" y "Game Over" se imprimen al final

        mock_print.assert_any_call('\nBlack wins')
        mock_print.assert_any_call("\nGame Over\n")

    @patch('game.interfaz.Interfaz.turn_menu', side_effect=[False])
    @patch('builtins.print')
    def test_start_game_turn_menu_false(self, mock_print, mock_turn_menu):
        interfaz = Interfaz()
        interfaz.start_game()
        # Verificar que turn_menu es llamado una sola vez
        self.assertEqual(mock_turn_menu.call_count, 1)

if __name__ == '__main__':
    unittest.main()