import random
x=[int(x) for x in input("enter 10 values :").split()]
p1=int(input("select a value in the list:"))
p2=int(input("select a value in the list:"))
random.shuffle(x)
if p1 in x :
    print("selected value" ,[p1])
else :
    print("invalid value")
if p2 in x :
    print("selected value" ,[p2])
else :
    print("invalid value")
r1=x.index(p1)
r2=x.index(p2)
print("####Game Over####")
if r1<r2:
    print("ranked of ur value :",r1)
    print("player 1 win")
else :
    print("ranked of ur value : ",r2)
    print("player 2 win")