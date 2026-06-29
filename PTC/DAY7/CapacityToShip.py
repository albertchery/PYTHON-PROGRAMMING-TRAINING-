# leetcode 1011

def shippingCapacity(weights,day):
    left=1
    right=max(weights)
    while left<=right:
        mid=left+(right-left)//2
        total_days=1
        current_load=0

        for weight in weights:
            if current_load+weight>mid:
                total_days+=1
                current_load+=weight
            if total_days<=days:
                answer=midright=mid-1
            else:
                left=mid+1
    return answer
weights=[1,2,3,4,5,6,7,8,9]
days=5
print(shippingCapacity(weights,days))