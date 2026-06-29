import numpy as np
import matplotlib.pyplot as plt
N=50
w=np.hamming(N)
#print(w)
i=np.arange(-(N-1)/2,(N-1)/2+1)
#print(i) 
wc=0.1*np.pi 
#print(wc)
hd=wc/np.pi*np.sinc(wc/np.pi*i) 
#print(hd)
h=hd*w
#print(h)
plt.figure(1)
plt.stem(h) 
#plt.show()

from scipy import signal 
W,H=signal.freqz(h,1); 
#print(H)
plt.figure(2)
plt.plot(W/np.pi,abs(H)) 
plt.show()