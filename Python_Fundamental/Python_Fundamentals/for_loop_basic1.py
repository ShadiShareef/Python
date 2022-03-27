for i in range(0,151):
    print(i)

for i in range(5,5001):
    if i%5==0:
        print(i)

for i in range(1,101):
    if i%10==0:
        print("Coding Dojo")
    elif i%5==0:
        print("Coding")

sumOdd=0
for i in range(0,500000):
    sumOdd+=i
print(sumOdd)

sum2018=0
for i in range(2018,0,-4):
    sum2018+=i
print(sum2018)

lowNum=1
highNum=50
mult=3
for lowNum in range(lowNum,highNum+1):
    if lowNum%mult==0:
        print(lowNum)