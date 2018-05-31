# -*- coding: utf-8 -*-
import pygame as pg
import numpy.random as rnd
import bouncing

pg.init()
running=True

black = (  0,   0,   0)
white = (255, 255, 255)
blue =  (  0,   0, 255)
green = (  0, 255,   0)
red =   (255,   0,   0)

xmax=800
ymax=800
reso=(xmax,ymax)

scr=pg.display.set_mode(reso)

t0=float(pg.time.get_ticks())/1000

ballimg=pg.image.load("ball1.gif")
ballimg=pg.transform.scale(ballimg,(25,25))
ballrect=ballimg.get_rect()

A=[0,0]
B=[xmax,0]
C=[xmax,ymax]
D=[0,ymax]
E=[rnd.rand() * xmax , rnd.rand() * ymax]
F=[rnd.rand() * xmax , rnd.rand() * ymax]


pos=[rnd.rand() * xmax , rnd.rand() * ymax]
vel=[rnd.rand() * 200, rnd.rand() * 200]


while running:
    pg.event.pump()
    keys=pg.key.get_pressed()
    
    t=float(pg.time.get_ticks())/1000
    dt=t-t0
    t0=t
    
    newpos=[pos[0]+vel[0]*dt,pos[1]+vel[1]*dt]
    
    anyBounce=False
    lines=[[A,B],[B,C],[C,D],[D,A],[E,F]]
    for line in lines:
        bounced,s,r,newv=bouncing.bounceline(line[0],line[1],pos,newpos,vel)
        if bounced:
            print('Bounce detected\npos=',pos,'\ns=',s,'\nr=',r,'\nv=',vel,'\nnewv=',newv)
            newpos=r
            vel=newv
            running=False
            break
        
    pos=newpos    

    ballrect.center=pos[0],pos[1]
    
    scr.fill(black)
    pg.draw.line(scr,red,A,B,5)
    pg.draw.line(scr,red,B,C,5)
    pg.draw.line(scr,red,C,D,5)
    pg.draw.line(scr,red,D,A,5)
    pg.draw.line(scr,red,E,F,5)

    scr.blit(ballimg,ballrect)
        
    pg.display.flip()
    
    if keys[pg.K_ESCAPE]:
        running=False

pg.quit()