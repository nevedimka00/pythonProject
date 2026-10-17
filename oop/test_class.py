from abc import ABC,abstractmethod

class UtilityTest:

    @staticmethod
    def add(a:int,b:int):
        return a+b
    
    @classmethod
    def deduct(cls,a:int,b:int):
        return a-b

    def __repr__(self)->str:
        return "This is a repr method"

    def __util__(self):
        return "This is new util dander method"


# ut = UtilityTest()
# res = ut.add(2,3)
# print(res)
# print(UtilityTest.deduct(5,3))
# print(str(ut))
# res2 = ut.deduct(9,4)
# print(res2)
# print(ut.__util__())

class AbsTest(ABC):

    @abstractmethod
    def must_do(self,text)->str:
        pass


class ChildOfAbs(AbsTest):

    __hidden_item = "hidden item"

    def __init__(self,name:str):
        super().__init__()
        self.name=name

    def must_do(self,text):
        return text

    def __getitem__(self, key):
        return self.__hidden_item if key=='item' else 'wrong key'
    
    def __setattr__(self, name, value):
        if not isinstance(value,str):
            return "WRONG TYPE"
        return super().__setattr__(name, value)

child = ChildOfAbs("alik")
# res = child.must_do(5)
# print(type(res))
# print(ChildOfAbs.mro())
# res2 = child.__getitem__('item')
# print(res2)

print(child.__setattr__("surname",6))
print(child.__setattr__("surname","petrosyan"))
print(child.surname)
