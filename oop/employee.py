class Employee:

    def __init__(self,name,position):
        self.name = name
        self.position=position

    def get_info(self):
        return f"{self.name} = {self.position}"

    @staticmethod
    def is_valid_position(position):
        valid_positions = ["manager","cashier","janitor"]
        return valid_positions.__contains__(position)

print(Employee.is_valid_position("driver"))
print(Employee.is_valid_position("cashier"))

emp1 = Employee("alik","manager")
emp2 = Employee("lera","supergirl")

res = emp1.is_valid_position(emp1.position)
print(res)