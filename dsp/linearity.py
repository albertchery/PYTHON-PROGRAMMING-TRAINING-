import numpy as np
x=np.array([1,2,3,4])
y=np.array([5,6,7,8])
a=5
b=7
from scipy import fft
LHS=abs(fft.fft(a*x+b*y))
RHS=abs((a*fft.fft(x))+(b*fft.fft(y)))
print("LHS   ",LHS,"\nRHS   ",RHS)