import math
bunches=[3,6,7,11]
h=8
left=1
right=max(bunches)
answer=right    
while left<=right:
    mid=left+(right-left)//2
    total_hours=0
    for bunch in bunches:
        total_hours=total_hours+math.ceil(bunch/mid)
    if total_hours<=h:
        answer=mid
        right=mid-1
    else:
        left=mid+1
print(answer)