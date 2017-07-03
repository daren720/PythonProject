
from Sprite import Sprite

import pygame
from pygame.locals import *
import GameTime

#==================================================================
class Shot( Sprite ):
    """description of class"""
    #==================================================================
    def __init__(self, imageList, xStart, yMax, speed, size ):
        Sprite.__init__(self, imageList )

        self.image = pygame.transform.scale(self.image, (size, size))
        self.rect = self.image.get_rect() 
        self.rect.x = float(xStart)
        self.rect.y = float(yMax )
        self.posX = float(xStart)
        self.posY = float(yMax )
        self.shotRate = speed

    #==================================================================
    def update( self ):
        Sprite.update( self )
        dt = GameTime.Delta()
        self.posY = self.posY - dt * self.shotRate





        



