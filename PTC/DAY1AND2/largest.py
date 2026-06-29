a=int(input("Enter the number"))
b=int(input("Enter the number"))
c=int(input("Enter the number"))
d=int(input("Enter the number"))
if(a>b and a>c and a>d):
    print(a," is the largest")
elif(b>c and b>d):
    print(b," is the largest")
elif(c>d):
    print(c," is the largest")
else:
    print(d," is the largest")   