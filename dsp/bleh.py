import numpy as np 
import matplotlib.pyplot as plt 
N=50 
w=np.hamming(N) 
i=np.arange(-(N-1)/2,(N-1)/2+1) 
wc=0.1*np.pi 
hd=wc/np.pi*np.sinc(wc/np.pi*i) 
h=hd*w 
plt.figure(figsize=(15,5)) 
plt.subplot(1,2,1) 
plt.stem(h) 
plt.title("impulse response") 
from scipy import signal 
W,H=signal.freqz(h,1); 
plt.subplot(1,2,2) 
plt.plot(W/np.pi,abs(H)) 
plt.title("Magnitude response") 
plt.show()