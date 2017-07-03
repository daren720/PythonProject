

import pygame
from pygame.locals import *

from Bubble import Bubble
from Group import Group
import GameTime
import random
from ManagerBase import ManagerBase



#==================================================================
class BubbleManager( ManagerBase ):
    """description of class"""

    #==================================================================
    def __init__(self, maxX, maxY ):
        ManagerBase.__init__( self )

        self.maxY = maxY
        self.maxX = maxX
        self.nextSpawnTime = GameTime.Time()

        self.imageSourceList = [    "bubble.png", "bubbleRed.png", 
                                    "bubbleGreen.png", "bubbleBlue.png", 
                                    "bubbleYellow.png", "bubblePurple.png", 
                                    "bubbleOrange.png" ]

        self.imageList = list()

        for i in self.imageSourceList:
            path = "Images/" + i
            self.imageList.append( pygame.image.load( path ).convert_alpha() )


    #==================================================================
    def update( self ):
       
        ManagerBase.update( self )

        if self.enable:
            if ( GameTime.Time() >= self.nextSpawnTime ):
                x = random.randint( 0, self.maxX )
                self.nextSpawnTime = GameTime.Time() + random.uniform( 0.1, 0.2 )
                size = random.randint( 16, 64 )
                speed = random.randint( 50, 500 )
                imageList = list()
                imageList.append( self.imageList[ random.randint( 0, len(self.imageList ) -1 )  ] )
                bubble = Bubble( imageList, x, speed, size )
                self.group.add( bubble )

        for b in self.group:
            if ( b.posY > self.maxY ):
                self.group.remove( b )







        



