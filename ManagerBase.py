

import pygame
from pygame.locals import *

from Bubble import Bubble
from Group import Group
import GameTime
import random



#==================================================================
class ManagerBase( ):
    """description of class"""
    def __init__(self ):
        self.group = Group()

        self.enable = False

    #==================================================================
    def Enable( self ):
        self.enable = True
   
    #==================================================================
    def Disable( self ):
        self.enable = False

    #==================================================================
    def KillAll( self ):
        self.group.empty()

    #==================================================================
    def GetGroup(self ):
        return self.group

    #==================================================================
    def update( self ):
      
        self.group.update()

    #==================================================================
    def Draw(self, displaySurface):
        self.group.draw(displaySurface)






        



