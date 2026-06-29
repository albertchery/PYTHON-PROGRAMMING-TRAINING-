products=eval(input("Enter the dictionary: "))
choice=input("KEY/PRICE")
def get_value(item):
    return item[1]
if choice=="KEY":
    sorted_dic=dict(sorted(products.items()))
    print("Sorted Dictionary: ",sorted_dic)
elif choice=="PRICE":
    sorted_dic=dict(sorted(products.items(),key=get_value))
    print(sorted_dic)

else:
    print("Invalid Choice")