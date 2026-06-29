n=float(input("units"))
if(n>200):
    bill=((100*1.5)+(100*2.5)+((n-200)*4)) #above 200 units 4rs
elif(n>100):
    bill=((100*1.5)+((n-100)*2.5))# above 100 units 2.5rs
else:
    bill=(n*1.5) #first 100 units 1.5 rs
print(bill)        