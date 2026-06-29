prices=[7,1,5,3,6,4]
current_sum=0
max_profit=0
for i in range(1,len(prices)):
    diff=prices[i]-prices[i-1]

    current_sum=max(0,current_sum+diff)
    max_profit=max(max_profit,current_sum)
print(max_profit)