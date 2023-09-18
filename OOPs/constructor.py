class Apple:
    def __init__(self,color,flavor):
        self.color = color
        self.flavor = flavor
    """Gives info about the color and flavor of the apple""" #This is a doc string and it is used with help
    # to give info about what the function does

jonagold = Apple("red", "sweet")

print(jonagold.color)
help(Apple)

