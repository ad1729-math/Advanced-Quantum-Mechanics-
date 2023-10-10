import numpy as np
from scipy.optimize import fsolve 
import matplotlib.pyplot as plt
import matplotlib.colors as colors

# a=1

# def f(k,x,B):
#     v=np.cos(k*a)-np.cos(x*a)+B*np.sin(x*a)/(x*a)#((k*a)**2/2-(k*a)**4/24+(k*a)**6/720)-B-((x*a)**2/2*(1-B/3)-(x*a)**4/24*(1-B/5)+(x*a)**6/720*(1-B/7))
#     return v

# def Root(k,B):
#     def f1(x):
#         return f(k,x,B)
#     x0=fsolve(f1,k/2)
#     return x0,x0**2


# K=np.linspace(0,20,1000)
# L1,L2=[],[]
# for k in K:
#     L1.append(Root(k,0.5)[1])
#     L2.append(Root(k,1)[1])

# plt.plot(K,L1,'r',label="$B=0.5$,$a=1$")
# plt.plot(K,L2,'b',label="$B=1$ ,$a=1$")
# plt.legend()
# plt.show()

u=5.7883818*10**-8
gN,gS=10**-4,2
P=gS-gN
A=545.8*10**6
h=6.636*10**(-34)

s=10**-18

def E44(B):
    x,A1=u*B/h*s,A*s
    E1,E2=A1*3.5-x*(7*gN+gS)/2,3.5*A1+x*(7*gN+gS)/2
    return [E1,E2]

def H(B):
    x,A1=u*B/h*s,A*s
    a1,b1,c1,d1=(3.5*A1-x*(3*gN+P*3/8)),x*np.sqrt(7)/8*P,x*np.sqrt(7)/8*P,(-4.5*A-x*(3*gN-P*3/8))
    a2,b2,c2,d2=(3.5*A1-x*(2*gN+P*1/4)),x*np.sqrt(3)/4*P,x*np.sqrt(3)/4*P,(-4.5*A-x*(2*gN-P*1/4))
    a3,b3,c3,d3=(3.5*A1-x*(gN+P*1/8)),x*np.sqrt(15)/8*P,x*np.sqrt(15)/8*P,(-4.5*A-x*(gN-P*1/8))
    a4,b4,c4,d4=(3.5*A1),x*P,x*P,(-4.5*A)
    a5,b5,c5,d5=(3.5*A1+x*(gN+P*3/8)),x*np.sqrt(7)/8*P,x*np.sqrt(7)/8*P,(-4.5*A+x*(3*gN-P*3/8))
    a6,b6,c6,d6=(3.5*A1+x*(gN+P*1/4)),x*np.sqrt(3)/4*P,x*np.sqrt(3)/4*P,(-4.5*A+x*(gN-P*1/4))
    a7,b7,c7,d7=(3.5*A1+x*(gN+P*1/8)),x*np.sqrt(15)/8*P,x*np.sqrt(15)/8*P,(-4.5*A+x*(gN-P*1/8))
    H=[[a1,b1,c1,d1],[a2,b2,c2,d2],[a3,b3,c3,d3],[a4,b4,c4,d4],[a5,b5,c5,d5],[a6,b6,c6,d6],[a7,b7,c7,d7]]
    return H


def Eigens(B,r):
    a,b,c,d=H(B)[r]
    return [((a+d)+np.sqrt((a+d)**2+4*b*c))/2,((a+d)-np.sqrt((a+d)**2+4*b*c))/2]

def Freq(B):
    M,W=[],[]
    for i in range(0,7):
        M.append(Eigens(B,i)[0])
        M.append(Eigens(B,i)[1])
    M.append(E44(B)[0])
    M.append(E44(B)[1])

    for n in range(len(M)):
        L=[]
        for j in range(n+1, len(M)):
            L.append(abs(M[j]-M[n])) #h has been taken care of here.
        W.append(L)
    return W


B=np.linspace(0,10,1000)
K=[]
for n in range(0,16):
    for j in range(0, 16-n-1):
       A0=[]
    #    print((n,j))
       v=Freq(0)[n][j]
       w=Freq(10)[n][j]-v
       if v>100:
           A0.append(v)
           A0.append(abs(w))
           A0.append([n,j])
        #    plt.plot(B,Freq(B)[n][j],'b')
       else:
           continue
       K.append(A0)
    #    plt.show()

# plt.show()
K0=[]
for l in range(len(K)):
    K0.append(K[l][1])

K1=np.sort_complex(K0)
# print(K1)
# print(K[K0.index(K1[1])])

List=[]
for n in range(0,16):
    for j in range(0,16-n-1):
        if Freq(0.01)[n][j]>10**8:
           List.append(Freq(0.01)[n][j])
        else:
            continue

L1=np.sort(List)
print(L1)






# plt.plot(B,Eigens(B,0)[0],'g',label="J=3")  #J=3 values
# plt.plot(B,Eigens(B,0)[1],'g',label="J=3")
# plt.plot(B,Eigens(B,1)[0],'r',label="J=2")  #J=2 values
# plt.plot(B,Eigens(B,1)[1],'r',label="J=2")   
# plt.plot(B,Eigens(B,2)[0],'b',label="J=1")  #J=1 values
# plt.plot(B,Eigens(B,2)[1],'b',label="J=1")
# plt.plot(B,Eigens(B,3)[0],'y',label="J=0")  #J=0 values
# plt.plot(B,Eigens(B,3)[1],'y',label="J=0")
# plt.plot(B,Eigens(B,4)[0],'k',label="J=-3")  #J=-3 values
# plt.plot(B,Eigens(B,4)[1],'k',label="J=-3")
# plt.plot(B,Eigens(B,5)[0],'m',label="J=-2")  #J=-2 values
# plt.plot(B,Eigens(B,5)[1],'m',label="J=-2")
# plt.plot(B,Eigens(B,6)[0],'c',label="J=-1")  #J=-1 values
# plt.plot(B,Eigens(B,6)[1],'c',label="J=-1")
# plt.plot(B,E44(B)[0],"darkblue",label="J=4")  #J=4 value
# plt.plot(B,E44(B)[1],'darkslategray',label="J=-4")  #J=-4 value
# plt.legend()
# plt.show()

