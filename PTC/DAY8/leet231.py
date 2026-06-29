def checkPowerOfTwo(n):
    return n>0 and (n&(n-1))==0
num=256
print(checkPowerOfTwo(num))