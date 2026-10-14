class Person:
    species = "humano"

    def __init__(self, name, age):
        self.name = name
        self.age = age

# Sirve para cambiar a todo a nivel de clase
    @classmethod
    def change_species(cls, new_species):
        cls.species = new_species

    @staticmethod
    def is_older(age):
        return age >= 18


person1 = Person("Benja", 22)
person2 = Person("dallas", 22)

print(person1.species)
print(person2.species)

Person.change_species("programador")

print(person1.species)
print(person2.species)

print(Person.is_older(22))
