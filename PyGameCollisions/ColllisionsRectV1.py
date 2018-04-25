#-*-coding:utf-8-*-
import pygame, sys, time
from pygame.locals import *

pygame.init()
FPS         = 30
fpsClock    = pygame.time.Clock()
winWidth    = 500
winHeight   = 500
mainSurface = pygame.display.set_mode((winWidth,winHeight),0,32)
pygame.display.set_caption('Collisions test')
background = pygame.image.load('images//bg1.jpg')

# Рисуем неподвижные компоненты на поверхности background
# Места расположения границ
border1Rect = pygame.Rect(0,0,100,500)
border2Rect = pygame.Rect(0,150,300,50)
# границы
border1 = pygame.draw.rect(background, (0,0,0), border1Rect, 0)
border2 = pygame.draw.rect(background, (0,0,0), border2Rect, 0)

# Подвижный блок
blockWidth  = 50
blockHeight = 50
blockColor  = (255,0,0)
# Начальные координаты подвижного блока - по центру 
blockX = (mainSurface.get_width() - blockWidth)/2
blockY = (mainSurface.get_height() - blockHeight)/2

direction = False

# описание функции --->
def newPosition(dirFlag, x, y):
    # Функция пересчитывает координаты для подвижного объекта
    if dirFlag:
        if dirFlag      == K_UP:
            y -= 5
        elif dirFlag    == K_DOWN:
            y += 5
        if dirFlag      == K_LEFT:
            x -= 5
        elif dirFlag    == K_RIGHT:
            x += 5
    return x, y
# --->

# Игра - цикл
while True:
    # Частота обновления экрана
    fpsClock.tick(FPS)

    # Рисуем неподвижные компоненты
    mainSurface.blit(background,(0,0))

    # просматриваем очередь событий
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

    # Рисуем подвижный компонент
    blockRect = pygame.Rect(blockX, blockY, blockWidth, blockHeight)
    block = pygame.draw.rect(mainSurface, blockColor, blockRect, 1)
     
    if blockRect.colliderect(border1Rect) or blockRect.colliderect(border2Rect) :
        print ("Столкновение (прямоугольные области пересеклись)")
    print (border1Rect, border1Rect, blockRect)

    # Рассчитываем новые координаты подвижного блока
    blockX, blockY = newPosition(direction, blockX, blockY)

    pygame.display.update()
