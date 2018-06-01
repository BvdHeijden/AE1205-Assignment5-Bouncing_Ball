# -*- coding: utf-8 -*-
#from numpy import *
from numpy.linalg import solve,norm
from numpy import dot
from numpy import *
import matplotlib.pyplot as plt

#calculate lambda and mu for a possible bounce
def intersect(a,b,p,q):
    x=[[b[0]-a[0],p[0]-q[0]],[b[1]-a[1],p[1]-q[1]]]
    y=[[p[0]-a[0]],[p[1]-a[1]]]
    z=solve(x,y)
    lam=z[0][0]
    mu=z[1][0]
    return lam,mu

#Calculate point of intersection
def intersectpoint(a,b,p,q):
    lam,mu=intersect(a,b,p,q)
    x=[b[0]-a[0],b[1]-a[1]]
    y=[lam*x[0],lam*x[1]]
    s=[a[0]+y[0],a[1]+y[1]]
    return s

#Calculate normal vector
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

#Calculate new position after bounce
def bouncedposition(a,b,p,q):
    s=intersectpoint(a,b,p,q)
    n=normalvec(a,b,p,q)
    
    x=[q[0]-s[0],q[1]-s[1]]
    x=dot(x,n)
    x=abs(x*2)
    qr=[x*n[0],x*n[1]]    
    r=[q[0]+qr[0],q[1]+qr[1]]
    return s, r

#Calculate new speed vector after bounce
def bouncedSpeed(v,n):
    dv=[2*abs(dot(v,n))*n[0],2*abs(dot(v,n))*n[1]]
    v=[v[0]+dv[0],v[1]+dv[1]]
    return v

#Main Bounce function
def bounceline(a,b,p,q,v):
    lam,mu=intersect(a,b,p,q)
    if lam>=0 and lam<=1 and mu>=0 and mu<=1:
        bounced = True
    else:
        bounced = False
        
    s,r=bouncedposition(a,b,p,q)
    newv=bouncedSpeed(v,normalvec(a,b,p,q))
    
    return bounced , s , r , newv
     
##Testcase to check bounce function   
#p1=[1.,4.]
#p2=[2.,1.]
#prevpos=[3.,6.] 
#pos=[1.,2.]
#v=[(pos[0]-prevpos[0])/0.1,(pos[1]-prevpos[1])/0.1]
#
#bounced,bouncepoint,newpos,newv=bounceline(p1,p2,prevpos,pos,v)
#
#plt.plot([p1[0],p2[0]],[p1[1],p2[1]],label="Line")
#plt.plot([prevpos[0],pos[0]],[prevpos[1],pos[1]],label="Original Trajectory")
#if bounced:
#    plt.plot([bouncepoint[0],newpos[0]],[bouncepoint[1],newpos[1]],label="Bounced Trajectory")
##    plt.plot([newpos[0],newpos[0]+newv[0]],[newpos[1],newpos[1]+newv[1]],label="new V")
#plt.legend()
#plt.axis("scaled")
#
#print((bounced,newpos,newv))   