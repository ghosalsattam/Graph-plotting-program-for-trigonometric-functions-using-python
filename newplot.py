import numpy as np
import matplotlib.pyplot as plt
from sympy import *
import math
import re





def formatFunc(value, tick_number):
    N =  value/np.pi
    if N == 0:
        return "0"
    else:
	return "$%.2f\pi $" % round(N,2)

ax=plt.axes()
ax.xaxis.set_major_formatter(plt.FuncFormatter(formatFunc))

def sin(lb,ub,x):
	y=np.sin(x)
	return y
		
def cos(lb,ub,x):
	y=np.cos(x)
	return y


def tan(lb,ub,x):
	if(ub-lb>=1000):
		print "Limit exceeded"
	y=np.tan(x)
	for i in range (len(y)-1):
		if(y[i+1]<y[i]):
			y[i]=y[i+1]=np.nan
	return y





s=raw_input("Enter the function ")
lb=float(input("Enter the lower bound "))
ub=float(input("Enter the upper bound "))
x=np.arange(lb,ub,.1)
for i in np.arange(int(lb/np.pi)*np.pi,int(ub/np.pi)*np.pi,np.pi/2):
	#print 'k'
	x=np.insert(x,1,i-.02)
	x=np.insert(x,1,i+.02)
	x=np.insert(x,1,i-.002)
	x=np.insert(x,1,i+.002)
x=np.sort(x)
y=np.empty(len (x))

cosec=np.empty(len(x))
cot=np.empty(len(x))
sec=np.empty(len(x))
if 'sin' in s or 'cosec' in s:
	sin=sin(lb,ub,x)

if 'cosec' in s:
	for i in range(len(sin)-1):
		if sin[i]*sin[i+1]<0:
			cosec[i]=cosec[i+1]=np.nan
		else:
			cosec[i]=1.0/sin[i]
	
if 'cos' in s or 'sec' in s:
	cos=cos(lb,ub,x)

if 'sec' in s:
	for i in range(len(cos)-1):
		if(cos[i]*cos[i+1]<0):
			sec[i]=sec[i+1]=np.nan
		else:
			sec[i]=1.0/cos[i]

if 'tan' in s or 'cot' in s:
	tan=tan(lb,ub,x)

if 'cot' in s:
	for i in range(len(tan)-1):
		if np.isnan(tan[i])==True:
			cot[i]=0
		elif tan[i]*tan[i+1]<0:
			cot[i]=cot[i+1]=np.nan
		else:
			cot[i]=1.0/tan[i]


if(ub-lb<1000):
	for i in range(len(x)):
		f=s
		
		
		if 'sin' in s:
			f=f.replace('sin x',str(sin[i]))
		if 'cosec' in s:
			f=f.replace('cosec x',str(cosec[i]))
		if 'cos' in s:	
			f=f.replace('cos x',str(cos[i]))
		if 'tan' in s:		
			f=f.replace('tan x',str(tan[i]))
		if 'sec' in s:
			f=f.replace('sec x',str(sec[i]))
		if 'cot' in s:
			f=f.replace('cot x',str(cot[i]))
		y[i]=simplify(f)
else:
	print "Limit exceeded"




for i in range(len(x)):
	if(y[i]>=100 or y[i]<=-100):
		y[i]=np.nan
plt.xticks(np.arange(int(lb/np.pi)*np.pi,int(ub/np.pi)*np.pi,np.pi/2),rotation=45)
plt.xlabel('time')
plt.grid()
plt.plot(x,y)
plt.show()
plt.close()
