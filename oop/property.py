class Rectangle:
    def __init__(self,width:int,height:int):
        self.width = width
        self._height = height


    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @width.setter
    def width(self,value):
        if(value<0):
            self._width=0
        else: self._width=value

    @height.deleter
    def height(self):
        del self._height

    def multiplier(func):
        def wrapper(self):
            print("multiplier worked")
            return func(self) * 2
        return wrapper

    def adder(value):
        def decorator_layer(func):
            def func_layer(self):
                print("adder worked")
                return func(self) + value
            return func_layer
        return decorator_layer

    @multiplier
    @adder(100)
    def area(self):
        return self.width* self.height

rect = Rectangle(2,4)
print(rect.area())

# print(rect._width)
# print(rect.width)

# del rect.height

# print(rect.height)
