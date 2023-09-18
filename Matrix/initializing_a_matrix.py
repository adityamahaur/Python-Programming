# import random
# M=[[random.randint(0,10) for x in range(4)]for y in range(5)]
# print(M)

R = int(input("rows = "))
C = int(input("coloumns = "))

M = [[0 for y in range(C)]for x in range(R)]
for r in range(R):
    for c in range(C):
        M[r][c] = int(input("input = "))
print("Matrix M is: ", M)