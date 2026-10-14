

class Person:
    species = "humana"

# self es como un this.
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # CUIDADO AL MANIPULAR ATRIBUTOS CUANDO TENGA _
        self._energy = 100
        # Atributo privado
        self.__password = "1234"

    def work(self):
        return f"{self.name} esta trabajando"

    def _waste_energy(self, quantity):
        self._energy -= quantity
        return self._energy


person1 = Person("Benjamin", 22)

person2 = Person("Dallas", 22)

print(person1.work())
print(person1._waste_energy(40))
print(person2.name)
print(person2._Person__password)
