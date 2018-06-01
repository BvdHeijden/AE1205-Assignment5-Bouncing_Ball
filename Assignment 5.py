# -*- coding: utf-8 -*-
import pygame as pg
import numpy.random as rnd
from numpy.linalg import norm
import bouncing

#Initialize Pygame and load ball image and sound
pg.init()
bounceSound=pg.mixer.Sound('bSound.wav')
ballimg=pg.image.load("ball1.gif")
ballimg=pg.transform.scale(ballimg,(25,25))
ballrect=ballimg.get_rect()
running=True

#Define Colors
black = (  0,   0,   0)
white = (255, 255, 255)
blue =  (  0,   0, 255)
green = (  0, 255,   0)
red =   (255,   0,   0)

#Set screen resolution
xmax=800
ymax=800
reso=(xmax,ymax)
scr=pg.display.set_mode(reso)

#Define lines (all four corners + 3 random lines)
A=[0,0]
B=[xmax,0]
C=[xmax,ymax]
D=[0,ymax]
E=[rnd.rand() * xmax , rnd.rand() * ymax]
F=[rnd.rand() * xmax , rnd.rand() * ymax]
G=[rnd.rand() * xmax , rnd.rand() * ymax]
H=[rnd.rand() * xmax , rnd.rand() * ymax]
I=[rnd.rand() * xmax , rnd.rand() * ymax]
J=[rnd.rand() * xmax , rnd.rand() * ymax]

#create a random starting position and velocity
pos=[rnd.rand() * xmax , rnd.rand() * ymax]
vel=[rnd.rand(), rnd.rand()]
vel=vel/norm(vel)*300

#set T0
t0=float(pg.time.get_ticks())/1000

#Main Loop
while running:
    pg.event.pump()
    pg.time.wait(5)
    keys=pg.key.get_pressed()
    
    #Calculate time since last frame
    t=float(pg.time.get_ticks())/1000
    dt=t-t0
    t0=t
    
    #Integrate velocity to get new position
    newpos=[pos[0]+vel[0]*dt,pos[1]+vel[1]*dt]
    
    #Check each line for a bounce, in which case calculate bounced position and velocity
    anyBounce=False
    lines=[[A,B],[B,C],[C,D],[D,A],[E,F],[G,H],[I,J]]
    for line in lines:
        bounced,s,r,newv=bouncing.bounceline(line[0],line[1],pos,newpos,vel)
        if bounced:
            pg.mixer.Sound.play(bounceSound)
            print('\nBounce detected\npos=',pos,'\ns=',s,'\nr=',r,'\nv=',vel,'\nnewv=',newv)
            newpos=r
            vel=newv
            break
        
    pos=newpos    
    
    #set new ball position
    ballrect.center=pos[0],pos[1]
    
    #re-draw screen
    scr.fill(black)
    pg.draw.line(scr,red,A,B,5)
    pg.draw.line(scr,red,B,C,5)
    pg.draw.line(scr,red,C,D,5)
    pg.draw.line(scr,red,D,A,5)
    pg.draw.line(scr,red,E,F,5)
    pg.draw.line(scr,red,G,H,5)
    pg.draw.line(scr,red,I,J,5)
    
    scr.blit(ballimg,ballrect)
        
    pg.display.flip()
    
    #quit when ESCAPE is pressed
    if keys[pg.K_ESCAPE]:
        running=False

pg.quit()