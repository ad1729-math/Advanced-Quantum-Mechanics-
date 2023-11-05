import math as m 
import numpy as np 
from scipy.integrate import dblquad
import cmath 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

j=complex(0,1)
h=10**(-8)

def E1(x,y,a):
    return ((a**2+2)-a*(np.cos(x)+np.cos(y))+2*np.cos(x)*np.cos(y))**0.5

def E2(x,y,a):
    return -((a**2+2)-a*(np.cos(x)+np.cos(y))+2*np.cos(x)*np.cos(y))**0.5

def X1(x,y,a):
    Psi=a-np.cos(x)-np.cos(y)
    Phi=np.sin(x)-j*np.sin(y)
    Abs=((E1(x,y,a)-Psi)**2+abs(Phi)**2)**0.5
    return [Phi/Abs, (E1(x,y,a)-Psi)/Abs]

def X2(x,y,a):
    Psi=a-np.cos(x)-np.cos(y)
    Phi=np.sin(x)-j*np.sin(y)
    Abs=((E2(x,y,a)-Psi)**2+abs(Phi)**2)**0.5
    return [Phi/Abs, (E2(x,y,a)-Psi)/Abs]

def IProd(X,Y):
    s=0
    for i in range(len(X)):
        s+=X[i].conjugate()*Y[i]
    return s 

def A1(x,y,a):
    X1x,X1y=[],[]
    for i in range(0,2):
        dx=(X1(x+h,y,a)[i]-X1(x,y,a)[i])/h
        dy=(X1(x,y+h,a)[i]-X1(x,y,a)[i])/h
        X1x.append(dx)
        X1y.append(dy)
    return [j*IProd(X1(x,y,a),X1x),j*IProd(X1(x,y,a),X1y)]


def A2(x,y,a):
    X2x,X2y=[],[]
    for i in range(0,2):
        dx=(X2(x+h,y,a)[i]-X2(x,y,a)[i])/h
        dy=(X2(x,y+h,a)[i]-X2(x,y,a)[i])/h
        X2x.append(dx)
        X2y.append(dy)
    return [j*IProd(X1(x,y,a),X2x),j*IProd(X1(x,y,a),X2y)]


def B1(x,y,a):
    Bxy=(A1(x+h,y,a)[1]-A1(x,y,a)[1])/h-(A1(x,y+h,a)[0]-A1(x,y,a)[0])/h
    return Bxy.real

def B2(x,y,a):
    Bxy=(A2(x+h,y,a)[1]-A2(x,y,a)[1])/h-(A2(x,y+h,a)[0]-A2(x,y,a)[0])/h
    return Bxy.real

def Chern(a):
    def B1a(x,y):
        return B1(x,y,a)
    def B2a(x,y):
        return B2(x,y,a)
    v1=dblquad(B1a,-np.pi,np.pi,-np.pi,np.pi)[0]
    v2=dblquad(B2a,-np.pi,np.pi,-np.pi,np.pi)[0]
    return [v1,v2]

print(Chern(1))


# # Define the function to be plotted

# # Generate a grid of x and y values
# x = np.linspace(-np.pi, np.pi, 100)  # Adjust the range and number of points as needed
# y = np.linspace(-np.pi, np.pi, 100)
# X, Y = np.meshgrid(x, y)
# Z1 = B1(X, Y ,2)
# Z2 = B2(X, Y ,2)
# # Create a 3D plot
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')

# # Plot the surface
# ax.plot_surface(X, Y, Z1, cmap='viridis')
# ax.plot_surface(X, Y, Z2, cmap='viridis')
# # Set labels for the axes
# ax.set_xlabel('X-axis')
# ax.set_ylabel('Y-axis')
# ax.set_zlabel('Z-axis')

# # Show the plot
# plt.show()
