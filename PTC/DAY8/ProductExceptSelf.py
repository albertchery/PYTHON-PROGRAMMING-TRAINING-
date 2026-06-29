def productExceptSelf(nums):
    n=len(nums)
    answer=[1]*n
    prefix=1
    # prefix array
    for i in range(n):
        answer[i]=prefix
        prefix=prefix*nums[i]
    suffix=1
    #suffix array
    for i in range(n-1,-1,-1):
        answer[i]=answer[i]*suffix
        suffix=suffix*nums[i]
    return answer
# MAIN
nums=[1,2,3,4]
print(productExceptSelf(nums))