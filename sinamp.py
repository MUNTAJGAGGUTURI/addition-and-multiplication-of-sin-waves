import numpy as np
from matplotlib import pyplot as plt
n=np.arange(1,500)
F=50;
Fs=1000;

s1=0.5*np.cos(2*np.pi*F/Fs*n+np.pi/2)
s2=0.5*np.cos(5*np.pi*F/Fs*n+np.pi/2)
s3=s1+s2;
plt.subplot(1,3,1)
plt.plot(n,s1);
plt.subplot(1,3,2)
plt.plot(n,s2)
plt.subplot(1,3,3)
plt.plot(n,s3)
plt.show()
