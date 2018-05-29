# -*- coding: utf-8 -*-
from numpy import *
from numpy.linalg import solve,norm

def intersect(a,b,p,q):
    x=[[b[0]-a[0],p[0]-q[0]],[b[1]-a[1],p[1]-q[1]]]
    y=[[p[0]-a[0]],[p[1]-a[1]]]
    z=solve(x,y)
    lam=z[0]
    mu=z[1]
    return lam,mu

def intersectpoint(a,b,lam):
    x=[b[0]-a[0],b[1]-a[1]]
    y=[lam*x[0],lam*x[1]]    
    s=[a[0]+y[0],a[1]+y[1]]
    return s


a=[1.,4]
b=[2.,1]
p=[3.,6]
q=[1.,2]

lam,mu=intersect(a,b,p,q)
s=intersectpoint(a,b,lam)
