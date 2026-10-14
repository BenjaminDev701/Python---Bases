

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def work(self):
        return f"{self.name} esta trabajando"


person1 = Person("Benjamin", 22)

person2 = Person("Dallas", 22)

print(person1.work())
print(person2.name)
