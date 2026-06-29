#DecodeWays
str="226"
n=len(str)
dp=[0]*(n+1)
# Initialization
dp[0]=1
dp[1]=1
for i in range (2,n+1):
    # single digit
    one_digit=int(str[i-1:i])
    if 1<=one_digit<=9:
        dp[i]=dp[i]+dp[i-1]
    #Two digit
    two_digit=int(str[i-2:i])
    if 10<=two_digit<=26:
        dp[i]=dp[i]+dp[i-2]
print(dp[n])