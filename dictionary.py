animals = {"bear": 4, "cat": 1, "Tiger": 10}

# "Tiger" in animals
# print(animals)
# for ani in animals:
#     print(ani)

# for ani, num in animals.items():
#     print("There are {} {}".format(num,ani))

# x = animals.values()

animals["cat"] = 7
animals["horse"] = 1
for x,y in animals.items():
    print(x, ":",y)