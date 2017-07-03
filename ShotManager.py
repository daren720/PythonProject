

import pygame
from pygame.locals import *

from Shot import Shot
from Group import Group
import GameTime
import random
from ManagerBase import ManagerBase



#==================================================================
class ShotManager( ManagerBase ):
    """description of class"""

    #==================================================================
    def __init__(self, maxX, maxY ):
        ManagerBase.__init__( self )

        self.maxY = maxY
        self.maxX = maxX
        self.nextShootTime = GameTime.Time()
        self.shoot = False
        self.shootPosX = 0
        self.shootPosY = 0

        self.imageSourceList = [    "Images/shot1.png" ]

        self.imageList = list()

        for i in self.imageSourceList:
            self.imageList.append( pygame.image.load( i ).convert_alpha() )

        self.shotSFX = pygame.mixer.Sound("Audio/lasershot.wav")

      


    #==================================================================
    def update( self ):
        if self.enable == False:
            return

        ManagerBase.update( self )

        if ( GameTime.Time() >= self.nextShootTime and self.shoot == True ):
            self.nextShootTime = GameTime.Time() + 0.4
            pygame.mixer.Sound.play(self.shotSFX)
            size = 12
            speed = 400
            image = self.imageList[ 0  ]
            offsetX = image.get_width() / 2.0
            shot = Shot( self.imageList, self.shootPosX - offsetX , self.shootPosY, speed, size )
            self.group.add( shot )

        for s in self.group:
            if ( s.posY < 0 ):
                self.group.remove( s )

        self.shoot = False

       
   
    #==================================================================
    def Shoot( self, rect ):
        if self.enable == False:
            return
        self.shoot = True
        self.shootPosX = rect.x
        self.shootPosY = rect.y
        






        



