#Créé par Rapha1111 et non Timothé

from math import *
from random import randint
import pygame
pygame.init()
taille=3
formatx,formaty=200,200
clock = pygame.time.Clock()

screen = pygame.display.set_mode((taille*formatx, taille*formaty))
def draw(screen, mapp, maxs, pos):
    mx,my=maxs
    screen.fill("white")
    for x in range(mx):
        for y in range(my):
            try:
                if mapp[x][y][0]==0:   continue
            except:
                print(x,y,mapp[x][y])
            pygame.draw.rect(screen, "yellow", (x*taille*formatx/mx, (my-y)*taille*formaty/my, taille*formatx/my, taille*formaty/my))
    pygame.draw.rect(screen, "red", ((pos[0])*taille*formatx/mx, (my-pos[1])*taille*formaty/my, taille*formatx/mx, taille*formaty/my))

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
            n.append((0,(0,0)))
        mp.append(n)
    return mp

def rdm(tx,ty):
    m=empty(tx,ty)
    for i in range(tx*ty//2):
        m[randint(0,tx-1)][randint(0,ty-1)]=(1, (0,0))
    return m


def update_map(mpp,mx,my):
    m=empty(mx,my)
    for x in range(mx):
        for y in range(my):
            if mpp[x][y][0]==0: continue #si il n'y a pas de particule a cette position
            (vx,vy)=mpp[x][y][1]
            if y<my-1: #si elle est pas au sol
                if mpp[x][y-1][0]==0: #si il n'y a pas de particule en dessous
                    if (vx,vy)==(0,0): #si la particule est stable
                        m[x][y]=(1,(0,-1)) #on fait prendre de la vitesse a la particule (on applique -g)
                        continue
                """if x-1<0 or x>mx: #si la particule est au bord
                    m[x][y]=(1,(0,0))
                    continue
                if mpp[x-1][y-1][0]==0: #si il n'y a pas de particule en diag bas gauche
                    m[x-1][y-1]=(1,(0,0))
                    continue
                if mpp[x+1][y-1][0]==0: #si il n'y a pas de particule en diag bas droite
                    m[x+1][y-1]=(1,(0,0))
                    continue"""
                #sinon, on execute la physique de la mecanique fondamentale, tah Newton et ses lois, en simplifié car j'ai la flm
                y+=vy
                vy-=1 #on retire g a la vitesse
                x+=vx
                if x<0: #si ca touche le bord gauche, ou rebondi
                    x=0
                    vx*=-1
                if x>mx-1: #de meme pour le droit
                    x=mx-1
                    vx*=-1
                if y<0:
                    y=1
                if y>my-1:
                    y=my-1
                
                while m[x][y][0]==1: #si il y a déjà une particule ici, on la met au dessus
                    y+=1
                    if y>my-1:
                        y=my-1
                        break
                    vx,vy=(0,0)
                m[x][y]=(1,(vx,vy))
                continue
            m[x][y]=(1,(0,0))
            continue
    return m
                    
def sign(n):
    if n>0:
        return 1
    return -1

def sable():
    mx,my=200,200
    mpp=rdm(mx,my)
    running=True
    px, py=mx//2,int(my*0.75)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
        draw(screen, mpp, (mx,my),(px,py))
        mpp=update_map(mpp, mx, my)
        if keydown(pygame.K_SPACE):
            if keydown(pygame.K_LSHIFT):
                for xx in range(-5,6):
                    for yy in range(-5,6):
                        mpp[px+xx*2][py+15+yy*2]=(1,(0,0))

            mpp[px][py]=(1,(0,0))
        if keydown(pygame.K_RETURN):
            for cx in range(-11, 12):
                for cy in range(-11, 12):
                    if 0 < px+cx < mx-1 and 0 < py+cy < my-1:
                        dist = sqrt(cx**2 + cy**2)
                        if dist < 3:  # détruit les particules au centre
                            mpp[px+cx][py+cy] = (0, (0,0))
                        elif dist < 10:  # propulse les particules proches
                            if cy<0: #le souffle de l'explosion ne pousse pas les particules en dessous
                                continue
                            vx = max(-5, min(5, int(10 * cx / dist)))
                            vy = max(-5, min(5, int(10 * cy / dist) * 3))
                            mpp[px+cx][py+cy] = (1, (vx, vy))
                            
        if keydown(pygame.K_DOWN):
            py-=1
            if py<0:
                py=0
        if keydown(pygame.K_UP):
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