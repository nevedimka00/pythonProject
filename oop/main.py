from car import Car


car1 = Car("ford",1960,"red",True)
car2 = Car("ferari",2000,"green",False)

# print(car1.color)

# car1.drive()
# car1.stop()

# print(car1)
# print(car1._Car__doors)
# print(Car.counter)

car1.surname = "Petrosyan"
Car.surname = "Horbachevska"

print(car1.surname)
print(Car.surname)
print(car2.surname)