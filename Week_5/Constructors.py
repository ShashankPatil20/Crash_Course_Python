class Person:
    def __init__(self, name):
        self.name = name
    def greeting(self):
        return "Hi, my name is " + self.name

new_person = Person("Kay")
print(new_person.greeting())

class Mango:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor

    def __str__(self):
        return "Mango is {} in a color and is {}".format(self.color, self.flavor)

Alphanso = Mango("Orange", "Sweet")
print(Alphanso)