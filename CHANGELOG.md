# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2024-08-08
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