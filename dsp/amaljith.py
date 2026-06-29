import numpy as np
n1=np.arange(0,3)
a1=(1/2)**n1
n2=np.arange(-2,1)
a2=(1/3)**n2
x=np.concatenate(a2,a1)
print(a1)
print(a2)
print(x)