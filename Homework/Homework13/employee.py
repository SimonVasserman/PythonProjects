from person import Person

class Employee(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.room = 0

    def __str__(self):
        return super().__str__() + f"\nroom: {self.room}"