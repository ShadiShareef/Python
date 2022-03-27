def biggie_size(c):
    for i in range(0,len(c)):
        if c[i]>0:
            c[i]="big"
    return(c)
print(biggie_size([1,2,3,-1,-3,0,1]))

def count_positives(c):
    x=0
    for i in range(0,len(c)):
        if c[i]>= 0:
            x+=1
    c[len(c)-1]=x
    return c
print(count_positives([1,2,3,4,5,-1,-2,-3]))

def sum_total(c):
    sum=0
    for i in range(0,len(c)):
        sum+=c[i]
    return sum
print(sum_total([1,2,3,4]))

def average(c):
    sum=0
    for i in range(0,len(c)):
        sum+=c[i]
    return sum/len(c)
print(average([1,2,3,4]))

def length(c):  
    if c==[]:
        return 0
    else:
        return len(c)
print(length([1,2,3,4,5]))

def min(c):  
    if c==[]:
        return False
    else:
        x=c[0]
        for i in range(0,len(c)):
            if x>c[i]:
                x=c[i]
        return x
print(min([1,2,3,4,5,2]))

def max(c):  
    if c==[]:
        return False
    else:
        x=c[0]
        for i in range(0,len(c)):
            if x<c[i]:
                x=c[i]
        return x
print(max([1,2,3,4,5,2]))

def ultimate_analysis(c):
    dictionary ={'sumTotal': sum_total(c),
        'average': average(c),
        'minimum': min(c), 
        'maximum': max(c),
        'length': length(c)}
    return dictionary
print(ultimate_analysis([37,2,1,-9]))

def revers(c):
    if len(c)==0:
        return "list is empty!"
    else:    
        for i in range(0,int(len(c)/2)):
            x=c[len(c)-1-i]
            c[len(c)-1-i]=c[i]
            c[i]=x
        return c
print(revers([1,2,3,4,5]))