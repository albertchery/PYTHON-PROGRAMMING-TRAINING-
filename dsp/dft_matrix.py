import numpy as np
import matplotlib.pyplot as plt
x=[0,1,2,1]    #x=np.array([)0,1,2,1])    correct method
#print(x)
n=4
tf=np.exp(-1j*2*np.pi/n)     #twiddle factor
D=np.empty((4,4),dtype=complex)
for i in range(0,4):
    for j in range(0,4):
        D[i,j]=tf**(i*j)
print("twiddle factor matrix :\n",np.round(D)) 

X=np.zeros(4,dtype=complex)
X=D@x           #np.array(x).T
print(X)

plt.figure (1) 
plt.subplot(2,1,1) 
plt.imshow(D.real) 
plt.title("Real part") 
plt.subplot(2,1,2) 
plt.imshow(D.imag) 
plt.title("Imaginary part") 

magnitude = np.abs(X) 
phase = np.angle (X) 
print("Magnitude :\n", np.round(magnitude),"\nPhase :\n", np.round(phase)) 
plt.figure(2) 
plt.subplot(2,1,1) 
plt.stem(magnitude) 
plt.subplot(2,1,2) 
plt.stem(phase) 
plt.show()
