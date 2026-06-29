import numpy as np
g=np.array([1,2,3,4])
h=np.array([5,6,7,8])
N=4
y=np.zeros(N)
htr=np.concatenate([[h[0]],h[N-1:0:-1]])
for i in range(0,4):
    y[i]=np.sum(g*htr)
    htr=np.roll(htr,1)
print(y)