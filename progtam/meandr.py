import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
from math import * 

t=np.linspace(-4,4,1000)
# T=np.linspace(tau,2*tau,100)
u0=1
def A(n):
	return 0#u0/pi**2/n**2*(cos(pi*n)-1)
def B(n):
	return 2*u0/pi/n*(1-cos(pi*n))

# def C(n):
	# return sqrt(A(n)**2+B(n)**2)
# def phi(n):
	# return np.arcsin(B(n)/sqrt(A(n)**2+B(n)**2))+pi/2+pi

u=A(1)*np.cos(1*t)+B(1)*np.sin(1*t)
# u=u+u0/4
i=1
print(i,A(i),B(i))
for i in range(2,100):
	print(i,A(i),B(i)/1.273)

	u=u+A(i)*np.cos(i*t)+B(i)*np.sin(i*t)
# Phi=phi(1)
# if Phi>pi:
# 	Phi=Phi-pi
# u=C(1)*np.sin(1*t+Phi)
# u=u+u0/4
# i=1
# print(i,C(i),Phi*180/pi)
# for i in range(2,100):
# 	Phi=phi(i)
# 	if Phi>pi:
# 		Phi=Phi-pi
# 	print(i,C(i),Phi*180/pi)
# 	u=u+C(i)*np.sin(i*t+Phi)

plt.plot(t,u)
plt.savefig('../plot/meandr.pdf', format='pdf')
# plt.show()
