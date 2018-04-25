# -*- coding: utf_8 -*-
import pygame, math
class myTimer:
# class - DOC
    """  class description
    myTimer - class - draw timer
    """
    pygame.init()
    
    def __init__ (self, bgColor, arrColor):
        print ("Class initialized")
        self.bgColor=bgColor
        self.arrColor=arrColor

    def __del__ (self):
        print ("Class deleted")

    def displayTimer(self, timerSurface, tim):
        #Analog
        timerSurface.fill((255,255,255))
        arrowColor = self.arrColor
        arrowLen = min(timerSurface.get_size())/2 - 10
        currentAngleInRadians = math.radians(tim)
        endX = timerSurface.get_width()/2 + arrowLen*math.cos(currentAngleInRadians)
        endY = timerSurface.get_height()/2 + arrowLen*math.sin(currentAngleInRadians)

        pygame.draw.ellipse(timerSurface, (self.bgColor), timerSurface.get_rect(), 1)
        pygame.draw.line(timerSurface, arrowColor , (timerSurface.get_width()/2, timerSurface.get_height()/2), (endX,endY), 2)

        #Digital
        pygame.font.init()
        txtSize =  int(timerSurface.get_height()/3)
        font = pygame.font.Font(pygame.font.match_font('arial'), txtSize)
        text = font.render(str (tim), 1, self.arrColor)
        timerSurface.blit(text,(15,15))

    
        
        return      

