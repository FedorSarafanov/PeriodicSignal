import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
from math import * 

t=np.linspace(-4,4,1000)
# T=np.linspace(tau,2*tau,100)
u0=1
def A(n):
	return 4*u0/pi**2*(1-cos(pi*n))/(n**2)

u=\
	A(1)*np.cos(1*t)+\
	A(2)*np.cos(2*t)+\
	A(3)*np.cos(3*t)+\
	A(4)*np.cos(4*t)+\
	A(5)*np.cos(5*t)+\
	A(6)*np.cos(6*t)+\
	A(7)*np.cos(7*t)+\
	A(8)*np.cos(8*t)+\
	A(9)*np.cos(9*t)+\
	A(10)*np.cos(10*t)

plt.plot(t,u)
plt.savefig('../plot/triangle.pdf', format='pdf')
# plt.show()
