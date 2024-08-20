class Piece:
    def __init__(self, color, position):
        self.__color__ = color
        self.__position__ = position
    
    
    def get_color(self):
        return self.__color__
    
    def get_position(self):
        return self.position

    def set_position(self, new_position):
        self.__position__ = new_position
        
    def __str__(self):
        return " "
    
    def check_move(self, new_position):
        return True