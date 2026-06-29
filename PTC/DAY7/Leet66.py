#Plus One
def plusOne(nums):
    n=len(nums)-1
    for i in range(n,-1,-1):
        if nums[i]<9:
            nums[i]+=1
            return nums
        nums[i]=0
    result=[0]*(len(nums)+1)
    result[0]=1
    return result
# MAIN
n=[1,2,3]
print(plusOne(n))