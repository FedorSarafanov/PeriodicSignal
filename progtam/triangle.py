from math import *
u0=pi**2/8

def A(n):
	return 4*u0/pi**2*(1-cos(pi*n))/(n**2)

for i in [1,2,3,4,5,6,7,8,9,10]:
	print(i,A(i))
