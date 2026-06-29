mm=float(input("Enter the amount of rain in mm:"))
if(mm<1 and mm>=0):
    print("No rain")
elif(mm<5 and mm>=1):
    print("Light rain")
elif(mm<10 and mm>=5):
    print("Moderate rain")
else:
    print("Heavy rain")