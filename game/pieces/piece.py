class Piece:
    def __init__(self, color, position):
        self.__color__ = color
        self.__position__ = position
    
    
    def get_color(self):
        return self.__color__
    
    def get_position(self):
        return self.__position__

    def set_position(self, new_position):
        self.__position__ = new_position
        
    def __str__(self):
        return " "
    
    def check_move(self, positions, new_position):
        return True