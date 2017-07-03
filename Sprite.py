import pygame
from pygame.locals import *

import GameTime

#==================================================================
class Sprite( pygame.sprite.Sprite ):
    """description of class"""

    #==================================================================
    def __init__( self, imageList, imageRate = 0.0, loop = False ):
        pygame.sprite.Sprite.__init__(self)
        
        self.imageList = imageList
        self.imageIndex = 0.0
        self.imageGameTime = 0.0
        self.imageRate = imageRate
        self.numImages = len( imageList )

        self.posX = 0.0
        self.posY = 0.0
        self.rect = pygame.Rect(0, 0, 10, 10 )
        self.rect.x = 0
        self.rect.y = 0

        self.image = self.imageList[ 0 ]

    def Init( self ):
        pass

    #==================================================================
    def GetImage(self, x, y, width, height):
        """ Grab a single image out of a larger spritesheet
            Pass in the x, y location of the sprite
            and the width and height of the sprite. """
 
        # Create a new blank image
        image = pygame.Surface([width, height]).convert()
 
        # Copy the sprite from the large sheet onto the smaller image
        image.blit(self.imageSheet, (0, 0), (x, y, width, height))
 
        # Assuming black works as the transparent color
        #image.set_colorkey(constants.BLACK)
 
        # Return the image
        return image

    #==================================================================
    def update( self ):

        # update the sprite animations to the next
        if self.numImages > 1:

            dt = GameTime.Delta()
            self.imageIndex = self.imageIndex + dt * self.imageRate
            if self.imageIndex > self.numImages:
                if self.looping:
                    self.imageIndex = 0 + ( self.numImages - self.imageIndex )
                else:
                    self.imageIndex = self.numImages - 1.0

            self.image = self.imageList[ int( self.imageIndex ) ]

        # update the position of the pygame sprite
        self.rect.x = self.posX
        self.rect.y = self.posY
    
    #==================================================================
    def GetMaxImages( self ):
        return self.numImages

    #==================================================================
    def GetCurrentImageIndex( self ):
        return self.imageIndex

    #==================================================================
    def GetImagesDone( self ):
        if self.looping:
            return False
        else:
            if self.GetCurrentImageIndex( ) >= self.GetMaxImages( )-1.0:
                return True
            else:
                return False




