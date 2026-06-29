n = int(input("Enter number of elements: "))

nums = []
for i in range(n):
    nums.append(int(input("Enter number")))
#nums=[3,2,3]
count=0
candidate=0
for num in nums:
    if count==0:
        candidate=num
    if num==candidate:
        count+=1
    else:
        count-=1
print(candidate)