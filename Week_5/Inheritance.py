class Fruit:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor

class Mango(Fruit):
    pass

class Orange(Fruit):
    pass

Alphanso = Mango("Orange", "Sweet")
print(Alphanso.color)

class Animals:
    sound = ""
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("{sound} I'm {name} {sound}".format(name=self.name, sound = self.sound))

class Lion(Animals):
    sound = "Grr"

Simba = Lion("Simba")
Simba.speak()


class Clothing:
    material = ""

    def __init__(self, name):
        self.name = name

    def checkmaterial(self):
        print("This {} is made of {}".format(self.name, self.material))


class Shirt(Clothing):
    material = "Cotton"


polo = Shirt("Polo")
polo.checkmaterial()