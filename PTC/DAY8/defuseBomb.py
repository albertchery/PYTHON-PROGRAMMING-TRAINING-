def defuseBomb(code,k):
    n=len(code)
    if k==0:
        return [0]*n
    ans=[0]*n
    for i in range(n):
        total=0
        if k>0:
            for j in range(1,k+1):
                total=total+code[(i+j)%n]
        else:
            for j in range(1,abs(k)+1):
                total+=code[(i-j+n)%n]
        ans[i]=total
    return ans
#MAIN
value=[5,7,1,4]
k=3
print(defuseBomb(value,k))