import unittest
from unittest.mock import patch, MagicMock
from game.interfaz import Interfaz

class TestInterfaz(unittest.TestCase):
    def setUp(self):
        self.__interfaz__ = Interfaz()

    @patch('builtins.input', side_effect=['1'])
    @patch('game.interfaz.Interfaz.start_game')
    def test_menu_start_game(self, mock_start_game, mock_input):
        self.__interfaz__.menu()
        mock_start_game.assert_called_once()

    @patch('builtins.input', side_effect=['2'])
    def test_menu_exit_game(self, mock_input):
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


'''
En proceso
'''

if __name__ == '__main__':
    unittest.main()