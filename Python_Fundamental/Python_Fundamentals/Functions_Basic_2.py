def countdown(a):
    z=[]
    for i in range(a,-1,-1):
        z.append(i)
    return z
z=countdown(5)
print(z)

def print_and_return(c):
    print(c[0])
    return c[1]
print_and_return([1,2])

def first_plus_length(c):
    print(c[0]+c[len(c)-1])
first_plus_length([1,2,3,4,5])

def values_greater_than_second(c):
    if len(c)<2:
        return False
    elif len(c)>=2:
        z=c[1]
        y=[]
        for i in range(0,len(c)):
            if c[i]>z:
                y.append(c[i])
    if y==[]:
        y="No Number Greater than the second"
        return y
    else :
        return y
print(values_greater_than_second([1,2,3,4,5,6]))

def length_and_value(a,b):
    z=[]
    for i in range(0,a):
        z.append(b)
    return z
print(length_and_value(6,2))
