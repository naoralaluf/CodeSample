
class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
    
    def __str__(self):
        return f"({self.x},{self.y})"
    
    def get_x(self):
        return self.__x
    
    def get_y(self):
        return self.__y
    
    def set_x(self, x):
        self.__x = x
    
    def set_y(self, y):
        self.__y = y
    
    @property
    def x(self):
        return self.get_x()
    
    @property
    def y(self):
        return self.get_y()
    
    @x.setter
    def x(self, x):
        self.set_x(x)
    
    @y.setter
    def y(self, y):
        self.set_y(y)
    
    def gradient(self):
        return self.y / self.x
    