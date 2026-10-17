class Animal:

    def __init__(self,name:str):
        self.name=name

    def to_speak(self):
        print("All Animals speak")

    def to_move(self):
        pass

    def to_fly(self):
        pass


class Cat(Animal):

    def __init__(self, name,color):
        super().__init__(name)
        self.color=color

    def to_speak(self):
        return super().to_speak()
    def to_move(self):
        print("Cat moves fast")


cat1 = Cat("buttons","grey")
cat1.to_move()
cat1.to_speak()
print(cat1.name)
print(cat1.color) 