def hashkey(myD, k):
    flag = k in myD
    if flag:
        print(myD, "has key", k)
    else: 
        print(myD, "doenst have key", k)

d1 = {'a':'apple', 'b':'Ball', 'c':'Cat'}
hashkey(d1,'a')
hashkey(d1, 'e')
    
    