import random
R = int(input("No. of rows = "))
C = int(input("No. of coloumns = "))

M = [[random.randint(0,20) for x in range(C)] for y in range(R)]
print(M)
# s=0
K = [[0 for x in range(C)]for y in range(R)]
for r in range(R):
    for c in range(C):
        if(M[r][c])%2 == 0: #true for even numbers
            # print('Add ',M[r][c])
            # s = s+ M[r][c]
            K[r][c] = M[r][c]
print(K)