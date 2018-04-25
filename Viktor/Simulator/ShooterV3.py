#-*-coding:utf-8-*-
import pygame , sys ,os, time
from pygame.locals import *
pygame.init()

""" Set initial data """
screenInfo = pygame.display.Info() # Get physical screen properties
#posX = screenInfo.current_w/10
posX = 0
#posY = screenInfo.current_h/10
posY = 0
sizeX = screenInfo.current_w-2*posX
sizeY = screenInfo.current_h-2*posY
bgColor = (255,255,255)
winCaptureText = "My game window"
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (posX, posY) # set pygame-window position

# Initialise pygame screen
screen = pygame.display.set_mode((sizeX, sizeY))
screen.fill(bgColor)
pygame.display.set_caption(winCaptureText)

#screen = pygame.display.set_mode((1000,600))
fpsclock  = pygame.time.Clock()

# Game speed
fps = 30

# Speeds
subSpeed = 1
shipSpeed = 2
planeSpeed = 3
missleSpeed = 5

# Directions
subDir = shipDir = planeDir = 1

# load images
sub         = pygame.image.load('images//sub2.png')
island      = pygame.image.load('images//island1.png')
plane       = pygame.image.load('images//plane.png')
ship        = pygame.image.load('images//ship_enemy1.png')
boomPict    = pygame.image.load('images//boom1.png')
boomPict = pygame.transform.scale(boomPict,(100,100))

waterColor  = (0,0,255)
skyColor    = (0,0,100)
seaLevel = screen.get_height()/2
toMove = 0
print (sizeY,screen.get_height() )
# Start submarine
subX = 0
subY = screen.get_height() - sub.get_height() - 200
subUp = 0

# Start ship
shipX = 0
shipY = seaLevel - ship.get_height()

# Start plane
planeX = 0
planeY = plane.get_height()

# Missle
planeMissleX = planeMissleY = 0
shipMissleX = shipMissleY = 0
shotToShip = shotToPlane = planeExploded = shipExploded = 0


#
planeBoomSteps = shipBoomSteps = 0
hideShip = hidePlane = 0 

def newPositions(subX, subY, shipX, shipY, planeX, planeY, shipMissleX, shipMissleY, planeMissleX, planeMissleY):
    # Calculate new positions function BEGIN
    global toMove, shotToShip, shotToPlane, planeExploded, shipExploded, screen, seaLevel, sub
    if toMove:
        # Submarine
        if toMove == K_w:
            if(subY > (seaLevel - sub.get_height()/2 )): subY -= subSpeed
        elif toMove == K_s:
            if(subY < (screen.get_height()-sub.get_height())): subY += subSpeed
        elif toMove == K_a:
            if(subX > 0):subX -= subSpeed
        elif toMove == K_d:
            if(subY < (screen.get_width()-sub.get_width())):subX += subSpeed

        # Missle start
        elif toMove == K_1:
            # Fire to plane
            shotToPlane = 1
            planeMissleX = subX + sub.get_width()
            planeMissleY = subY

        elif toMove == K_2:
            # Fire to ship
            shotToShip = 1
            shipMissleX = subX + sub.get_width()
            shipMissleY = subY 

    # Missle move
    if (shotToPlane):
        planeMissleY -= missleSpeed
        if (planeExploded):
            # Reset plane boom
            shotToPlane = 0

    if (shotToShip):
        shipMissleX += missleSpeed
        if(shipExploded):
            # reset ship boom
            shotToShip = 0
    
    # Ship move
    shipX   += shipSpeed
    if (shipX > screen.get_width()):
        shipX = 0
        planeExploded = 0
    
    # Plane move
    planeX  += planeSpeed 
    if (planeX > screen.get_width()):
        planeX = 0
        shipExploded = 0

    return   subX, subY, shipX, shipY, planeX, planeY, shipMissleX, shipMissleY, planeMissleX, planeMissleY
    # Calculate new positions function END    

while 1:
    fpsclock.tick(fps)
    screen.fill((255,255,255))

    # Get keyboard event
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            toMove = event.key
        if event.type == KEYUP:
            toMove = 0
            
    # Save old coordinates for:
    #  ship shipOldX, shipOldY
    #  plane planeOldX, planeOldY 
    #  submarine subOldX, subOldY
    #  missle missleOldX, missleOldY
    #

    (subOldX, subOldY, shipOldX, shipOldY, planeOldX, planeOldY, shipOldMissleX, shipOldMissleY, planeOldMissleX, planeOldMissleY) = (subX, subY, shipX, shipY, planeX, planeY, shipMissleX, shipMissleY, planeMissleX, planeMissleY)

    # Count new coordinates for:
    #  ship shipX, shipY
    #  plane planeX, planeY 
    #  submarine subX, subY
    #  missle missleX, missleY
    #

    (subX, subY, shipX, shipY, planeX, planeY, shipMissleX, shipMissleY, planeMissleX, planeMissleY) = newPositions(subX, subY, shipX, shipY, planeX, planeY, shipMissleX, shipMissleY, planeMissleX, planeMissleY)

    # Draw sky
    sky = pygame.draw.rect(screen,skyColor,[0,0,screen.get_width(),seaLevel])
        
    # Draw water
    water = pygame.draw.rect(screen,waterColor,[0,seaLevel,screen.get_width(),screen.get_height()])
    
    # Draw island
    screen.blit(island,(450,210))

    if (not hideShip):
        if (shipExploded):
            # Display ship BOOM
            screen.blit(boomPict,(shipX,shipY))
            shipBoomSteps += 1
            if(shipBoomSteps >= 50):
                hideShip = 1
                shipBoomSteps   = 0
                shipExploded    = 0
                shipRect = (0,0,1,1)
                continue # Выходим из IF , не переходя к рисованию корабля
        else :
            # Display ship
            shipRect = screen.blit(ship,(shipX, shipY))
            print (hideShip, shipRect, shipExploded)

    if (not hidePlane):
        if (planeExploded ):
            # Display plane BOOM
            screen.blit(boomPict,(planeX,planeY))
            planeBoomSteps += 1
            if(planeBoomSteps >= 50):
                hidePlane = 1
                planeBoomSteps  = 0
                planeExploded   = 0
                planeRect = (0,0,1,1) 
                continue
        else :
            # Display plain
            planeRect = screen.blit(plane,(planeX, planeY))

    # Draw submarine
    screen.blit(sub,(subX,subY))
    
    # missles
    if (shotToPlane):
        misslePlaneRect = pygame.draw.circle(screen,(255,255,0),(planeMissleX, planeMissleY), 5, 0)
        planeExploded   = misslePlaneRect.colliderect(planeRect)
        
    if (shotToShip):
        missleShipRect  = pygame.draw.circle(screen,(255,0,0),  (shipMissleX, shipMissleY), 5, 0)
        shipExploded    = missleShipRect.colliderect(shipRect)
   
    pygame.display.flip()
    pygame.display.update()
