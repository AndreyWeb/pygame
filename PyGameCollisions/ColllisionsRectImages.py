#-*-coding:utf-8-*-
import pygame, sys, time
from pygame.locals import *

pygame.init()
FPS=30
fpsClock=pygame.time.Clock()
width=500
height=500
mainSurface=pygame.display.set_mode((width,height),0,32)
pygame.display.set_caption('Столкновения')

background=pygame.image.load('images//bg1.jpg')
sprite = pygame.image.load('images//pict2.gif')     # Подвижная картинка
sprite2 = pygame.image.load('images//pict2.gif')    # Неподвижная картинка


# Начальные координаты подвижной картинки - по центру 
spritex=(mainSurface.get_width() - sprite.get_width())/2
spritey=(mainSurface.get_height() - sprite.get_height())/2

direction=False

# --->
def move(direction, spritex, spritey):
    # Функция пересчитывает координаты для подвижного объекта
    if direction:
        if direction == K_UP:
            spritey-=5
        elif direction == K_DOWN:
            spritey+=5
        if direction == K_LEFT:
            spritex-=5
        elif direction == K_RIGHT:
            spritex+=5
    return spritex, spritey
# --->

# game loop
while True:
    fpsClock.tick(FPS) # Частота обновления экрана
    mainSurface.blit(background,(0,0))
    # Место расположения подвижной картинки
    rect1 = pygame.Rect(spritex,spritey,sprite.get_width(), sprite.get_height())
    mainSurface.blit(sprite,(rect1.x,rect1.y))
    # Место расположения неподвижной картинки
    rect2 = pygame.Rect(0,00,sprite2.get_width(), sprite2.get_height())

    mainSurface.blit(sprite2,(rect2.x,rect2.y))
    
     
    if rect1.colliderect(rect2):
        print ("Столкновение (прямоугольные области пересеклись)")
        print (rect1)
        print (rect2)
        

    # get all events from the queue
    for event in pygame.event.get():
        # loop events queue, remember in 'direction' pressed key code
        if event.type == QUIT:
            # window close X pressed
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            # ESC key pressed
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN: direction = event.key # Other key pressed
        if event.type == KEYUP:  direction = False # Key released

    # calculate new image position

    spritex, spritey = move(direction, spritex, spritey)

    pygame.display.update()
