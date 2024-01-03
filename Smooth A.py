import math as m 
import numpy as np 
import matplotlib.pyplot as plt 

E0,s=3,0.5
def G(x,a,s):
    return np.exp(-(x-a)**2/s**2/2)

def A(x):
    return (x+10)**0.8*0.05+0.05
E=np.linspace(E0-5,E0+5,50)
C,A0=[],[]
for e in E:
    c=G(e,E0,s)+np.random.uniform(0,0.2)
    C.append(c)
    A0.append(A(e))

plt.plot(E,C,'ro',label="$|C_m|^2$")
plt.plot(E,A0,'bo',label="$A_{mm}(E)$")
plt.ylim([0,1])
plt.xlim()
plt.title('Distribution of $|C_m|^2$')
plt.legend()
plt.show()