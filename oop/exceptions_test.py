
class MyOwnException(Exception):
    def __str__(self):
        return "Age must be more than 18"


try:
    number = int(input("Enter a number: "))
    print(1/number)
    if(number<18): raise MyOwnException()
    secnd_number = number + "number"
except (ZeroDivisionError, ValueError) :
    print("Please enter a correct value")
except TypeError:
    print("This was a type error")
except MyOwnException as error :
    print(error)
finally: print("This is a final code")