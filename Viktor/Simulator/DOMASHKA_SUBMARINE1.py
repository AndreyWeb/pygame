#-*-coding:utf-8-*-
import pygame , sys ,time
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((1000,600))
fps = 30
fpsclock  = pygame.time.Clock()
sub = pygame.image.load('images//sub2.png')
#sub = pygame.transform.scale(screen,(100,30))
island = pygame.image.load('images//island1.png')
plane = pygame.image.load('images//plane.png')
ship1 = pygame.image.load('images//ship_enemy1.png')
boomPict = pygame.image.load('images//boom1.png')
boomPict = pygame.transform.scale(boomPict,(100,100))
boomStart = 0                         


watercolor = (0,0,255)
skycolor = (0,0,100)
direction = 0

mStep = 2
dxf = 1
xfly = 0
angle = 0
xship = 300
dxsw = 0
dxsw = 1
seaLevel = 240

subX = screen.get_width() - sub.get_width()
subY = screen.get_height() - sub.get_height()
subX = 50
subY = 500
submarineUnderwater = True

# rocket
rX = rY = 0

rocketCondition = False 


#--block limitator
blocks = []
block1 = pygame.Surface((1000,10))
block1.set_alpha(0)
#block1.fill((255,0,0))
block1Rect = pygame.Rect(0,270,block1.get_width(), block1.get_height())
blocks.append((block1,block1Rect))
def moving(directtion , subY,subX):
    global rocketCondition, submarineUnderwater, rX, rY
    if direction:
        if directtion == K_w:
            subY -= mStep
        elif direction == K_s:
            subY += mStep
        elif direction == K_a:
            subX -= mStep
        elif direction == K_d:
            subX += mStep
        elif direction == K_1:
            angle = 180
        elif direction == K_r:
            # check submarine underwater position and set submarineUnderwater = True (or False)
            if (submarineUnderwater):
                rocketCondition = True
                # remember current submarine X
                rX = subX
                rY = subY
    return   subY , subX

def collision():
    global blocks
    global spriteRectNew
    colFlag = False
    #-- checking collision
    for block in blocks:
        if spriteRectNew.colliderect(block[1]):
            collisionDIrect = direction
            colFlag = True
    return colFlag
"""
def rocketMove(x):
    
    return rX 
"""        
while True:
    fpsclock.tick(fps)
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            direction = event.key
        if event.type == KEYUP:
            direction = 0

    #remember block pos
    #block1X = blocks[0][1][0]
    #lock1Y = blocks[0][1][1]
    #block1oldXY = (block1X,block1Y)
    oldPos = (subX, subY)
    spriteRect = (subX,subY)

        
            
    sky = pygame.draw.rect(screen,skycolor,[0,0,1000,600])
        
    water = pygame.draw.rect(screen,watercolor,[0,300,1000,300])
    screen.blit(island,(450,210))
    
    screen.blit(sub,(subX,subY))
    
    # move submarine
    subY,subX = moving(direction , subY,subX)


    #Calling collisions--

    spriteRectNew = pygame.Rect(subX,subY,sub.get_width(), sub.get_height())
    if collision():
        (subX,subY) = oldPos
    for block in blocks:
        screen.blit(block[0],(block[1].x,block[1].y))
    
    # Move plain
    xfly += dxf
    flying = screen.blit(plane,[xfly,70])
    if (xfly <0 or xfly > (1000 - int(flying[2]+dxf))):
        dxf *= -1

    # Move ship
    xship +=dxsw
    ship_moving = screen.blit(ship1,[xship,240])
    if (xship < 0 or xship > (1000 - int(ship_moving[2]+dxsw))):
        dxsw *= -1


    # move  Rocket
    
    if (rocketCondition):
        # change coords
        rX += +10
        print rX
        print rY
        # check target collision
        rocketRect = (rX, rY )
        rocketRect = pygame.draw.circle(screen,(255,0,0), (rX, rY), 5, 0)
        boom = rocketRect.colliderect(ship_moving)
        shipSaved = ship1
        if (boom and ship1 == shipSaved) :
            print ("Boom!!")
            # change ship image
            # skip 100 game loops
            # freeze ship moving
            # return ship image
            ship1 = boomPict
            boomStart += 1
            if (boomStart > 100):
                print(boomStart)
                print(boom)
                boom = False
                ship1 = shipSaved
                boomStart = 0
            
            
    
    #--bliting block--
    
    pygame.display.flip()
    pygame.display.update()
