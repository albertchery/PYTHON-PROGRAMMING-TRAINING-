import numpy as np
x=np.array([1,1,2,1,2,2,1,1])
n=8
y=np.zeros(8,dtype=complex)
for i in range(0,8):
    #print(x[i])
    for j in range(0,8):
        y[i]=y[i]+x[j]*np.exp(-1j*2*np.pi*j*i/n)
print(np.round(y))

from scipy import fft
X=fft.fft(x)
print(np.round(X))