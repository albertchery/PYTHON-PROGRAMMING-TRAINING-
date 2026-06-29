n=int(input("Enter the num of tickets"))
p=float(input("Enter the price of the ticket"))
cat=int(input("Enter category: 1: Student   2:Person"))
if(n>=15 and cat==1):
    disc=p*0.25 #20% discount
    p=p-disc
    print("Price per student:",p)
elif(n<15 and cat==1):
    disc=p*0.05  #5% discount
    p=p-disc
    print("Price per student:",p)
if(n>=15 and cat==2):
    disc=p*0.1   #10% discount
    p=p-disc
    print("Price per person:",p)
else:
    print(p)
totalamount=n*p
print("Total Amount:  ",totalamount)