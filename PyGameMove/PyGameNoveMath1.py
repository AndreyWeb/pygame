import pygame, sys, time, math
from pygame.locals import *
gameSpeed = 50
winWidth, winHeght  = 800, 600
toMove  = False
# при нажатии на SPACE - старт
# шаг для актёра
actorStep = 1

pygame.init()
gameWin = pygame.display.set_mode((winWidth, winHeght),0,32)
gameFPS = pygame.time.Clock()
pygame.display.set_caption('Keyb jump, moves')
background=pygame.image.load('images//bg1.jpg')
actor = pygame.image.load('images//pict2.gif')
scale = int(gameWin.get_width()/10)
actor = pygame.transform.scale(actor, (50,50))

# Актёра ставим в центр экрана
#x0 = x = (gameWin.get_width() - actor.get_width())/2
x0 = x = 0
#y0 = y = (gameWin.get_height() - actor.get_height())/2
y0 = y = gameWin.get_height() - actor.get_height()

# --->
def actorPosition (x, y):
    global n , x0, y0, toMove, actorStep 
    # Рассчитываем новые координаты актёра
    if(toMove):
        if toMove == K_SPACE:
            dd = n*actorStep
            #x = x0 + 0*dd + dd*dd/20
            #y = y0 - 5*dd
            #x = 300 + math.sqrt(abs(100-dd*dd))    
            #y = 300 - math.sqrt(abs(100-dd*dd))
            # ellipse 
            #x = 300 + (math.cos(math.radians(dd)) * 100)
            #y = 300 + (math.sin(math.radians(dd)) * 200)
            # sin
            x = dd
            y = 300 + (math.sin(math.radians(dd)) * 150)

            print("X Y")
            print (x,-(y-550))
            
    return x, y
# --->


# game loop
n=0
while True:
    gameFPS.tick(gameSpeed) # кадров в сек - скорость игры
    gameWin.blit(background,(0,0))
    gameWin.blit(actor,(x,y))
    n+=1

    for event in pygame.event.get():
        #  Просмотр очереди событий Запоминаем кож клавиши в toMove
        if event.type==QUIT:
            # Нажали - закрыть окно
            pygame.quit()
            sys.exit()
        if event.type==KEYDOWN and event.key == K_ESCAPE:
            # Нажали ESC 
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN: toMove = event.key  # Нажали клавишу - запомнили какую именно
        #if event.type == KEYUP:   toMove = False      # Отпустили клавишу - остановиться
        if event.type == KEYDOWN and event.key == K_1:   toMove = False      # Отпустили клавишу - остановиться

    # пересчёт координат актёра    
    x, y = actorPosition (x, y)

    pygame.display.update()
