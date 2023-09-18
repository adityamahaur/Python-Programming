#immutable lists are called tuples
animals = ["Lion", "Zebra", "Dolphin", "Monkey"]
chars = 0
for animal in animals:
    chars += len(animal)

print("Total characters: {}, Average length: {}".format(chars, chars/len(animals)))




winners = ['Ashley', 'Bob', 'William', 'John']
for index, person in enumerate(winners):
    print("{} - {}".format(index+1, person))