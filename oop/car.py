class Car:
    wheels:int = 4
    __doors=2
    counter=0
    surname = ""

    def __init__(self,model:str,year:int,color:str,for_sale:bool):
        self.model=model
        self.year=year
        self.color=color
        self.for_sale=for_sale
        Car.counter+=1

    def drive(self):
        print(f"I am driving {self.model}")

    def stop(self):
        print("I stoped the car")

    def __str__(self):
        return (f"Model : {self.model} , Year : {self.year}, Color : {self.color} , For_Sale : {self.for_sale}")