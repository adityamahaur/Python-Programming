import random
D = int(input("Enter the dimension of the matrix = "))
M = [[random.randint(10,100) for x in range(D)]for y in range(D)]
print(M)

for r in range(D):
    for c in range(D):
        if r>c: #for lower triangle matrix we can keep the condition to be r<c
            M[r][c] = 0
        
print("Upper traiangle Matrix is: ")
for i in range(D):
    print(M[i])