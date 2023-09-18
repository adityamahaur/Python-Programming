# name = "Manny"
# number = len(name) * 3
# print("Hello {}, you lucky number is {}".format(name,number))


# price = 7.5
# with_tax = price *1.09
# print(price,with_tax)
# print("base price: {:.2f}, with taxes: {:.2f}".format(price,with_tax))

def to_celcius(x):
    return (x-32)*5/9

for x in range(0,101,10):
    print("{:>3} F | {:>6.2f} C".format(x,to_celcius(x))) # > is used for right allign 