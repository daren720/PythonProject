
from Sprite import Sprite

import pygame
from pygame.locals import *
import GameTime

#==================================================================
class Direction():
    NONE = 0,
    LEFT = 1,
    RIGHT = 2
    
#==================================================================
class Ship( Sprite ):
    """description of class"""
    #==================================================================
    def __init__(self, imageList, maxX, maxY, xStart, yStart, size ):
        Sprite.__init__(self, imageList )

        self.image = pygame.transform.scale(self.image, (size, size))
        self.rect = self.image.get_rect()
        self.xStart = xStart
        self.yStart = yStart
        self.rect.x = float(xStart)
        self.rect.y = float(yStart)
        self.posX = float(xStart)
        self.posY = float(yStart)
        self.move = Direction.NONE
        self.moveRate = float(300)
        self.maxX = maxX
        self.maxY = maxY

    #==================================================================
    def Reset( self ):
        self.rect.x = float(self.xStart)
        self.rect.y = float(self.yStart)
        self.posX = float(self.xStart)
        self.posY = float(self.yStart)

    #==================================================================
    def update( self ):
        Sprite.update( self )
        dt = GameTime.Delta()
        if self.move == Direction.LEFT:
             self.posX = self.posX - dt * self.moveRate
             if self.posX < 10.0:
                 self.posX = 10.0
        if self.move == Direction.RIGHT:
             self.posX = self.posX + dt * self.moveRate
             if self.posX > self.maxX - self.image.get_width() - 10:
                 self.posX = self.maxX - self.image.get_width() - 10
        
        self.move = Direction.NONE

    #==================================================================
    def Left( self ):
        self.move = Direction.LEFT
    #==================================================================
    def Right( self ):
        self.move = Direction.RIGHT
    #==================================================================
    def GetPos( self ):
        rect = pygame.Rect(0, 0, 0, 0)
        rect.x = self.posX + (self.image.get_width() / 2.0)
        rect.y = self.posY - 10
        return rect





        



