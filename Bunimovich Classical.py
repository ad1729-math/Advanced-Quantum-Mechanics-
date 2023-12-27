import numpy as np
import matplotlib.pyplot as plt

R,L=1,2
dt=0.001
g=0

Xb= np.linspace(-L - R, L + R, 1000)
Ybp, Ybm = [], []

T0 = 100

for x in Xb:
    if abs(x)<= L:
        Ybp.append(R)
        Ybm.append(-R)
    else:
        Ybp.append(np.sqrt(R**2-(abs(x)-L)**2))
        Ybm.append(-np.sqrt(R**2-(abs(x)-L)**2))

x0,y0,vx0,vy0=0,0,np.pi,0.1
T=np.linspace(0,T0,int(T0/dt))

Pos,Vel=[[x0,y0]],[[vx0,vy0]]

for t in T:
    x,y=Pos[-1][0],Pos[-1][1]
    vx,vy=Vel[-1][0],Vel[-1][1]
    
    if abs(x) <= L:
        if y > R - vy * dt:
            x, y = x + vx * dt, 2 * R - y - vy * dt
            vy = -vy
        elif y<-R-vy*dt:
            x, y = x + vx * dt, -2 * R - y - vy * dt
            vy=-vy
        else:
            x,y=x+vx*dt, y+vy*dt
            vy=vy-g*dt
    else:
        if x > L:
            if (x - L + vx * dt)**2 + (y + vy * dt)**2 >= R**2:
                dt1 = (R**2 - ((x - L)**2 + y**2)) / (2 * (vx * (x - L) + vy * y))
                x, y = x + vx * dt1, y + vy * dt1
                vr = (vx * (x - L) + vy * y) / R
                vq = (-y * vx + (x - L) * vy) / R
                vx, vy = -vr * ((x - L) / R) - vq * (y / R), -vr * (y / R) + vq * ((x - L) / R)
                x, y = x + vx * (dt - dt1), y + vy * (dt - dt1)
            else:
                x,y=x+vx * dt, y + vy * dt
        else:
            if x < -L:
                if (x + L + vx * dt)**2 + (y + vy * dt)**2 >= R**2:
                    dt1=(R**2 - ((x + L)**2 + y**2)) / (2 * (vx * (x + L) + vy * y))
                    x,y=x+vx * dt1, y + vy * dt1
                    vr=(vx*(x+L)+vy*y)/R
                    vq=(-y*vx+(x+L)*vy)/R
                    vx,vy=-vr*((x+L)/R)-vq*(y/R),-vr*(y/R)+vq*((x+L)/R)
                    x,y=x+vx*(dt-dt1),y+vy*(dt - dt1)
                else:
                    x,y=x+vx*dt, y+vy*dt

    Pos.append([x, y])
    Vel.append([vx, vy])

X, Y = [], []
for i in range(len(T)):
    X.append(Pos[i][0])
    Y.append(Pos[i][1])

plt.plot(Xb,Ybp,'b')
plt.plot(Xb,Ybm,'b')
plt.plot(X,Y,'r')
plt.xlim([-(R + L)-0.5,R+L+0.5])
plt.ylim([-R-0.5,R+0.5])
plt.show()
