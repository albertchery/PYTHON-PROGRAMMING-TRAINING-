a=int(input("Enter the number"))
b=int(input("Enter the number"))
c=int(input("Enter the number"))
if(a>b and a>c):
    if(b>c):
        print(b," is second largest")
    else:
        print(c,"is second largest")
elif(b>c and b>a):
    if(c>a):
        print(c ,"is the 2nd largest")
    else:
        print(a, "is the 2nd largest")
#else: