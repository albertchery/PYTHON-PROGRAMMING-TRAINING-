import numpy as np
g=np.array([1,2,3,4])
h=np.array([5,6,7,8])
N=4

y=np.zeros(N) 
Htr=np.concatenate([[h[0]],h[N-1:0:-1]]) 
for n in np.arange(N):
    y[n]=np.sum(Htr*g) 
    Htr=np.roll(Htr,1) 
print(y)

#using dft function
from scipy import fft
G=fft.fft(g)
H=fft.fft(h)
I=fft.ifft(G*H)
print(I)