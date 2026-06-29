def climbingStairs(n):
    if n==1 or n==0:
        return 1
    return climbingStairs(n-1)+climbingStairs(n-2)
print(climbingStairs(4))