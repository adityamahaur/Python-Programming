import random

R = int(input("Dimension of square Matrix = "))
C = R  # For diagonals you need a square matrix and in a square matrix R=C
d1 = []  # First diagonal
d2 = []  # Second diagonal
M = [[random.randint(10, 99) for x in range(C)] for y in range(R)]
for i in range(R):
    print(M[i])
for r in range(R):
    for c in range(C):
        if r == c:
            d1.append(M[r][c])
        if r + c == R - 1:
            d2.append(M[r][c])
print("Diagonal d1 is = ", d1)
print("Diagonal d2 is = ", d2)
