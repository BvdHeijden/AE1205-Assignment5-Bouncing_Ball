# -*- coding: utf-8 -*-
#from numpy import *
from numpy.linalg import solve,norm
from numpy import dot,sqrt
from numpy import *
import matplotlib.pyplot as plt

def intersect(a,b,p,q):
    x=[[b[0]-a[0],p[0]-q[0]],[b[1]-a[1],p[1]-q[1]]]
    y=[[p[0]-a[0]],[p[1]-a[1]]]
    z=solve(x,y)
    lam=z[0][0]
    mu=z[1][0]
    return lam,mu

def intersectpoint(a,b,p,q):
    lam,mu=intersect(a,b,p,q)
    x=[b[0]-a[0],b[1]-a[1]]
    y=[lam*x[0],lam*x[1]]
    s=[a[0]+y[0],a[1]+y[1]]
    return s

def normalvec(a,b,p,q):
    n1=[-1*(b[1]-a[1]),(b[0]-a[0])]
    n2=[(b[1]-a[1]),-1*(b[0]-a[0])]
    
    a=[q[0]-p[0],q[1]-p[1]]
    
    
    if dot(a,n1) < 0:
        n=n1
    else:
        n=n2
    
    n=n/norm(n)
       
    return n

def bouncedposition(a,b,p,q):
    s=intersectpoint(a,b,p,q)
    n=normalvec(a,b,p,q)
    
    x=[q[0]-s[0],q[1]-s[1]]
    x=[x[0]*n[0],x[1]*n[1]]
    x=[x[0]*2,x[1]*2]
    
    qr=[x[0]*n[0],x[1]*n[1]]
    return qr





    
a=[1.,4]
b=[2.,1]
p=[3.,6]
q=[1.,2]
    

s=intersectpoint(a,b,p,q)
n=normalvec(a,b,p,q)
qr=bouncedposition(a,b,p,q)


plt.plot([a[0],b[0]],[a[1],b[1]],label="AB")
plt.plot([p[0],q[0]],[p[1],q[1]],label="PQ")
plt.plot([s[0],s[0]+n[0]],[s[1],s[1]+n[1]],label="N")
plt.plot([q[0],q[0]+qr[0]],[q[1],q[1]+qr[1]],label="QR")
plt.legend()