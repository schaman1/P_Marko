#Créé par Rapha1111 et non Timothé

from math import *
from random import randint
import pygame
pygame.init()
taille=3
formatx,formaty=320,224
clock = pygame.time.Clock()

screen = pygame.display.set_mode((taille*formatx, taille*formaty))
def draw(screen, mapp, pos):
    screen.fill("white")
    mi, ml=len(mapp), len(mapp[0])
    for i in range(mi):
        for l in range(ml):
            if mapp[i][l]==1:
                pygame.draw.rect(screen, "yellow", (i*taille*formatx/mi, l*taille*formaty/ml, taille*formatx/mi+1, taille*formaty/ml+1))
    pygame.draw.rect(screen, "red", (pos[0]*taille*formatx/mi, pos[1]*taille*formaty/ml, taille*formatx/mi+1, taille*formaty/ml+1))

    pygame.display.flip()
def keydown(k):
  keys = pygame.key.get_pressed()
  if keys[k]:
    return True
  return False
def empty(tx,ty):
    mp=[]
    for x in range(tx):
        n=[]
        for y in range(ty):
            n.append(0)
        mp.append(n)
    return mp

def rdm(tx,ty):
    m=empty(tx,ty)
    for i in range(tx*ty//2):
        m[randint(0,tx-1)][randint(0,ty-1)]=1
    return m


def update_map(mpp):
    m=empty(len(mpp), len(mpp[0]))
    for x in range(len(mpp[0])):
        for y in range(len(mpp)):
            if mpp[y][x]==0:
                continue
            if x<len(mpp)-1:
                if mpp[y][x+1]==0:
                    m[y][x+1]=1
                elif mpp[y-1][x+1]==0:
                    m[y-1][x+1]=1
                elif y<len(mpp[0])-1 and mpp[y+1][x+1]==0:
                    m[y+1][x+1]=1
                else:
                    m[y][x]=1
            else:
                m[y][x]=1
    return m
                    

def sable():
    mx,my=200,200
    mpp=rdm(mx,my)
    running=True
    px, py=100,20
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
        draw(screen, mpp,(px,py))
        mpp=update_map(mpp)
        if keydown(pygame.K_SPACE):
            if mpp[px][py]==0:
                if keydown(pygame.K_LSHIFT):
                    for xx in range(-5,6):
                        for yy in range(-5,6):
                            mpp[px+xx*2][py+10+yy*2]=1

                mpp[px][py]=1
            else:
                for cx in range(-11,12):
                    for cy in range(-11,12):
                        if 0<px+cx<mx-1 and 0<py+cy<my-1:
                            if sqrt(cx**2+cy**2)<10:
                                mpp[px+cx][py+cy]=0
        if keydown(pygame.K_UP):
            py-=1
            if py<0:
                py=0
        if keydown(pygame.K_DOWN):
            py+=1
            if py>my-2:
                py=my-2
        if keydown(pygame.K_LEFT):
            px-=1
            if px<0:
                px=0
        if keydown(pygame.K_RIGHT):
            px+=1
            if px>mx-2:
                px=mx-2
        
        
        clock.tick(60)

sable()