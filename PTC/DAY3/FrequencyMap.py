numbers=list(map(int,input("Enter values:").split()))
k=int(input("Enter the threshold value k:"))
freq=dict()
for num in numbers:
    freq[num]=freq.get(num,0)+1
for num,count in freq.items():
    if count>k:
        print(f"{num}:{count} times") 