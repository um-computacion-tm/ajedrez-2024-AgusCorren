# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.3.0] - 2024-08-22
### Agregando
- **tests/test_interfaz.py**:
  - Añadidos tests para la clase `Interfaz`, aún sigue en proceso.
- **tests/test_bishop.py**:
  - Añadidos tests para la clase `Bishop`.
- **tests/test_king.py**:
  - Añadidos tests para la clase `King`.
- **tests/test_knight.py**:
  - Añadidos tests para la clase `Knight`.
- **tests/test_pawn.py**:
  - Añadidos tests para la clase `Pawn`.
- **tests/test_piece.py**:
  - Añadidos tests para la clase `Piece`.
- **tests/test_queen.py**:
  - Añadidos tests para la clase `Queen`.
- **tests/test_rook.py**:
  - Añadidos tests para la clase `Rook`.
### Modificando
- **game/chess_game.py**:
  - Método `validate_cords` para validar las coordenadas de las piezas.
  - Método `print_board` para imprimir el tablero de ajedrez.
  - Método `own_pieces` para obtener la pieza que posee el usuario.
- **game/board.py**:
  - Método `color_pieces` para obtener el color de la pieza en una posición.
- **pieces/**: Implementado método para validar si un movimiento es válido.
  - Método `check_move` en cada clase de pieza para validar si un movimiento es válido.
- **game/exceptions.py**: Implementando nuevas excepciones.
  - Excepción `InvalidPieceMovement` para errores de movimientos de piezas.
  - Excepción `ColorError` para errores de piezas de color diferente.
## [0.2.0] - 2024-08-15
### Agregando
- **chess_game.py**:
  - Método `move` para mover piezas en el tablero, con validación de coordenadas.
  - Método `change_turn` para alternar entre los turnos de los jugadores (blanco y negro).
- **exceptions.py**: Implementado excepciones para los errores que pueden ocurrir en el juego.
- **test_chess.py**: Implementado test unitarios para  la clase `Chess`.
- **test_board.py**: Implementado test unitarios la clase `Board`.
### Modificando
- **pieces/**: Implementado los metodos para mover las piezas.
  - Método `get_position` en cada clase de pieza para obtener la posición de la pieza.
  - Método `set_position` en cada clase de pieza para establecer la posición de la pieza.
- **cli.py** -> **interfaz.py**: Renombrado del archivo `cli.py` a `interfaz.py` y reformado para implementar la clase `Interfaz` que gestiona la interacción del usuario con el juego.
  - Método `menu` para mostrar la interfaz de línea de comandos.
  - Método `validate_option` para validar las opciones del menú.
  - Método `start_game` para iniciar el juego.
- **board.py**: Modificado tablero inicial para el juego.
  - Metodo `find_piece` que busca la posición de una pieza en el tablero.
  - Método `move` para mover piezas en el tablero, con validación de coordenadas.
  - Método `validate_move` para validar si un movimiento es válido.
  - Método `execute_move` para ejecutar el movimiento en el tablero.
- **main.py**: Implementado archivo principal para ejecutar el juego.
- **.coveragerc**: Modificado para correr los test unitarios.
## [0.1.0] - 2024-08-13
### Agregando
- **chess.py**: Implementada la clase `Chess` que gestiona el tablero y el turno de los jugadores.
  - Método `move` para mover piezas en el tablero, con validación de coordenadas.
  - Método `change_turn` para alternar entre los turnos de los jugadores (blanco y negro).
- **cli.py**: Creada una interfaz de línea de comandos (CLI) básica para interactuar con el juego de ajedrez.
  - Función `main` que inicializa el juego.
  - Función `play` que gestiona la interacción del usuario para mover piezas en el tablero.
- **board.py**: Creado un tablero inicial para el juego.
  - Método `get_piece` que obtiene la pieza que se encuentra en x posicion.
- **Dockerfile**: Para crear un entorno contenedor para ejecutar el proyecto en Python.
## [0.0.1] - 2024-08-08
### Agregando
- Integracion con CircleCI.
- Intregración con CodeClimate.
- Archivo README con información básica.
- Archivo CHANGELOG para registrar cambios.
- Archivo main.py con función working() para probar la funcionalidad.
- Archivo test_example.py con test unitarios para probar la funcionalidad.
