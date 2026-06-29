def palindromeCheck(x):
    reversed=0
    if x<0 or (x%10==0 and x!=0):
        return False
    while x>reversed:
        digit=x%10
        reversed=reversed*10+digit
        x//10
    return True
    return x==reversed or x==reversed//10
    
x=123
print(palindromeCheck(x))