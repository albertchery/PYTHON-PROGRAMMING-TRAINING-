numbers=list(map(int,input("Enter the number:").split()))
if len(numbers)==len(set(numbers)):
    print(False)
else:
    print(True)