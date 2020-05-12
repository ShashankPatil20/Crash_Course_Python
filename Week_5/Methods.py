class Piglet:
    def speak(self):
        print("Oink Oink")

Hamlet = Piglet()
Hamlet.speak()

class Piggy:
    name = "Swig"
    def speaking(self):
        print("Hi, I am {}".format(self.name))

Hammy = Piggy()
Hammy.speaking()
Hammy.name = "Jammy"
Hammy.speaking()

class Pig:
    years = 0
    def Count_year(self):
        return self.years*18

Pigy = Pig()
Pigy.years = 2
print(Pigy.Count_year())


class Dog:
    years = 0

    def dog_years(self):
        return self.years * 7

fido = Dog()
fido.years = 3
print(fido.dog_years())