import pygame, sys, time, math
from pygame.locals import *
gameSpeed = 50
winWidth, winHeght  = 600, 600
toJump = toMove  = False
# при нажатии на SPACE - прыгаем
# параметры прыжка: шагов - maxJumpSteps, рвзмер шага по X - jumpDX , Y - jumpDX
jumpDX = 5
jumpDy = 30
maxJumpSteps = 10
jumpStep = 0
# шаг для актёра
actorStep = 1

pygame.init()
gameWin = pygame.display.set_mode((winWidth, winHeght),0,32)
gameFPS = pygame.time.Clock()
pygame.display.set_caption('Keyb jump, moves')
background=pygame.image.load('images//bg1.jpg')
actor = pygame.image.load('images//pict2.gif')
scale = int(gameWin.get_width()/10)
actor = pygame.transform.scale(actor, (scale,scale))

# Актёра ставим в лев нижн точку экрана
x = 0
y0 = y = (gameWin.get_width() - actor.get_width())

# --->
def actorPosition (x, y):
    # Рассчитываем новые координаты актёра
    global y0, toJump, toMove, jumpDX, jumpDy, maxJumpSteps, jumpStep
    if(toMove and not toJump):
        if toMove == K_LEFT:
            x -= actorStep
            print ("left")
        if toMove == K_RIGHT:
            x += actorStep
            print ("right")
        if toMove == K_SPACE:
            # Jump
            y0 = y
            toJump = True
            print ("jump")

    if(toJump):
        jumpStep += 1 
        x += jumpDX
        y -= jumpDy 
        # завершение прыжка
        if (jumpStep > maxJumpSteps) :
            # прыжок закончен
            y = y0
            jumpStep = 0
            toJump = False
            toMove = True
    return x, y
# --->

# game loop
while True:
    gameFPS.tick(gameSpeed) # кадров в сек - скорость игры
    gameWin.blit(background,(0,0))
    gameWin.blit(actor,(x,y))

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
        if event.type == KEYUP:   toMove = False      # Отпустили клавишу - остановиться

    # dspsdftv пересчёт координат актёра    
    x,y = actorPosition (x, y)

    pygame.display.update()
