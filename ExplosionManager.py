



import pygame
from pygame.locals import *

from Group import Group
from ManagerBase import ManagerBase


#==================================================================
class ExplosionManager( ManagerBase ):
    """description of class"""

    #==================================================================
    def __init__(self ):
        ManagerBase.__init__( self )

    #==================================================================
    def Add( self, sprite ):
        self.group.add( sprite )
        self.enable = False

    #==================================================================
    def update( self ):
     
        ManagerBase.update( self )

        for s in self.group:
           if s.GetImagesDone():
               self.group.remove( s )        


 






        



