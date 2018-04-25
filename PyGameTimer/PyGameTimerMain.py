# -*- coding: utf_8 -*-
import pygame
from PyGameTimerClass import *

# Init pygame screen
pygame.init()
size = width, height = 600, 400
bgColor = (255, 255, 255)
screen = pygame.display.set_mode(size)
screen.fill(bgColor)

# Create new surface
surface1 = pygame.Surface((300,150))
surface1.fill((255,255,255))
surface1.set_alpha(150)
surface2 = pygame.Surface((300,300))
surface2.fill((0,100,0))
surface2.set_alpha(150)

timer1 = myTimer((255,0,0),(0,0,255))
timer2 = myTimer((255,0,255),(0,255,255))

myTime = 0
myGame = True 
clock = pygame.time.Clock()
while myGame:
    clock.tick(1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: myGame = False
            
    # Draw timer
    myTime += 1
    timer1.displayTimer(surface1, myTime)
    timer2.displayTimer(surface2, myTime)
    screen.blit(surface1,(0,0))
    screen.blit(surface2,(100,100))
    pygame.display.flip()


pygame.quit()
