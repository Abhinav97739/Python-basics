def fact(integer):
    multiply=1
    for i in range(integer,1,-1):
        multiply*=i
    return multiply
print(fact(5))
