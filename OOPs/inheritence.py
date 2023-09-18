# class Fruit:
#     def __init__(self,color,flavor):
#         self.color = color
#         self.flavor = flavor
# class Apple(Fruit):
#     pass
# class Grape(Fruit):
#     pass

#Inheriting animal class into piglet and cow class to use the same attributes
class Animal:
    sound = " "
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("{sound} I'm {name}! {sound}".format(name = self.name, sound = self.sound))

class piglet(Animal):
    sound = "oink!"

hamlet = piglet("hamlet")
hamlet.speak()

class cow(Animal):
    sound = "Moooo!"

Milky = cow("Milky")
Milky.speak()