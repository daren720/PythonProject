
from Sprite import Sprite

import pygame
from pygame.locals import *
import GameTime

#==================================================================
class ShipExplosion( Sprite ):
    """description of class"""
    #==================================================================
    def __init__(self, xStart, yStart ):

        self.imageList = list()
        
        self.imageSheet = pygame.image.load( "Images/shipExplosion.png" ).convert_alpha()
        for y in range( 0, 3 ):
            for x in range( 0, 3 ):
                image = self.GetImage( x * 64, y * 64, 64, 64 )
                image = pygame.transform.scale( image, (128, 128))
                
                self.imageList.append( image )

        Sprite.__init__(self, self.imageList)

        self.rect = self.image.get_rect() 
        self.rect.x = float( xStart - self.rect.width / 2.0)
        self.rect.y = float( yStart )
        self.posX = float(self.rect.x)
        self.posY = float(self.rect.y)

        self.imageRate = 10
        self.looping = False

    #==================================================================
    def update( self ):
        Sprite.update( self )
      




