class Point:
    # Constructor
    def __init__(self):
        self.__x = 0
        self.__y = 0
    
    # Get string version
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
    