# print(type(0))
# print(type("a"))
# print(dir(""))
# print(help(""))

# class Apple:
#     color = " "
#     flavour = " "
# jonagold = Apple()
# jonagold.color = "red"
# jonagold.flavour = "sweet"
# print(jonagold.color)
# print(jonagold.flavour)

class Piglet:
    name = "Piglet"
    def speak(self):
        print("oink! I'm {}! oink!".format(self.name))
    years = 0
    def pig_years(self):
        return self.years * 18
hamlet = Piglet()
hamlet.name = "hamlet"
hamlet.speak()
pentunia = Piglet()
pentunia.name = "Pentunia"
pentunia.speak()

piggy = Piglet()
piggy.years = 2
print(piggy.pig_years())

hamlet.years = 5
print(hamlet.pig_years())
