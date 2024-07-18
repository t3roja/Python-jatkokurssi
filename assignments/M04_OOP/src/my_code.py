import math

class Point:

    xCount = 0 # point counter initializion


    def __init__(self, x,  y):
        self._x = x
        self._y = y

    @property
    def x(self):
        Point.xCount += 1 # add one to point counter
        return self._x
    
    @x.setter
    def x(self, value):
        self._x = value
    
    @property
    def y(self):
        Point.xCount += 1
        return self._y
    
    @y.setter
    def y(self, value):
        self._y = value

    @staticmethod
    def getter_count():
        return Point.xCount
    
    @staticmethod
    def closest(p_list):

        def distance_to_origin(point):
            return math.sqrt(point.x**2 + point.y**2)
        
        closest_point = min(p_list, key=distance_to_origin)
        return distance_to_origin(closest_point)
        
    
#Write test software under this if
if __name__ == "__main__":
    print(f"Point got count: {0}", Point.getter_count())
    point1 = Point(-1, 7)
    print(point1.x)
    print(point1.x, point1.y)
    print(f"Point got count: {Point.getter_count()}")

