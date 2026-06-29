w=int(input("Enter number of wheels:"))
v=int(input("Enter number of vehicles:"))
for x in range(0,v+1):
    y=v-x
    if (4*x+2*y==w):
        print("No. of two wheelers:",y)
        print("No. of four wheelers:",x)