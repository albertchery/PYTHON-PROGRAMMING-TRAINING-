day=input("Enter the day").split()
attendees=int(input("Enter the number of attendees:"))
def classifySuccessOfParty(day,attendees):
    weekdays=["Monday","Tuesday","Wednesday","Thursday"]
    weekends=["Friday","Saturday","Sunday"]
    if day not in weekdays and day not in weekends:
       return"Invalid day"
    if day in weekdays:
        if 700<=attendees<=1000:
            return "Successful"
        else:
            return "unsuccessful"
    if day in weekends:
        if attendees>=1500:
            return "Successfuul"
        else:
            return "Unsuccessful"
result=classifySuccessOfParty(day,attendees)
print(result)