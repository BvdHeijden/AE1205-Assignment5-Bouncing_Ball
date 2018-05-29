# -*- coding: utf-8 -*-
from numpy import *
from numpy.linalg import solve

def intersect(a,b,p,q):
    x=[[b[0]-a[0],p[0]-q[0]],[b[1]-a[1],p[1]-q[1]]]
    y=[[p[0]-a[0]],[p[1]-a[1]]]
    z=solve(x,y)
    return z

