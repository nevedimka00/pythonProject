
from abc import ABC,abstractmethod

# ABSTRACT BASE CLASS
class Shape(ABC):

    # abstract method every child should implement
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):

    def area(self):
        print("inherited abstract method")


class ShapeUser:
    def __init__(self,obj:Shape):
       obj.area()


circle = Circle()
shape_user = ShapeUser(circle)