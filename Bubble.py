
from Sprite import Sprite

import pygame
from pygame.locals import *
import GameTime

 #==================================================================
class Bubble( Sprite ):
    """description of class"""
     #==================================================================
    def __init__(self, imageList, xStart, speed, size ):
        Sprite.__init__(self, imageList)

        self.image = pygame.transform.scale(self.image, (size, size))
        self.rect = self.image.get_rect() 
        self.rect.x = float(xStart)
        self.rect.y = 0
        self.posX = float(xStart)
        self.posY = float(0)
        self.fallRate = speed


     #==================================================================
    def update( self ):
        Sprite.update( self )
        dt = GameTime.Delta()
        self.posY = self.posY + dt * self.fallRate





