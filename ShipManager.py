import pygame
from pygame.locals import *

from Ship import Ship
from Group import Group
import GameTime
import random
from ManagerBase import ManagerBase


#==================================================================
class ShipManager( ManagerBase ):
    """description of class"""

    #==================================================================
    def __init__(self, maxX, maxY, lives ):
        ManagerBase.__init__( self )

        self.maxY = maxY
        self.maxX = maxX
        self.lives = lives
        self.imageList = list()
        self.imageList.append( pygame.image.load( "Images/SpaceCraft.png" ).convert_alpha() )
        
        size = 64
        offsetY = 50
        self.ship = Ship( self.imageList, self.maxX, self.maxY, maxX / 2, maxY - size - offsetY, size )
        self.group.add( self.ship )


    #==================================================================
    def Reset( self ):
        self.ship.Reset()

    #==================================================================
    def GetPos( self ):
        return self.ship.GetPos()

    #==================================================================
    def update( self ):
        if self.enable == False:
            return

        ManagerBase.update( self )


    #==================================================================
    def Left( self ):
        if self.enable == False:
            return
        self.ship.Left()

    #==================================================================
    def Right( self ):
        if self.enable == False:
            return
        self.ship.Right()




