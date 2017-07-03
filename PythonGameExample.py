



import pygame
from pygame.locals import *

from Bubble import Bubble
from Group import Group
from BubbleManager import BubbleManager
from ShipManager import ShipManager
from ShotManager import ShotManager
from ShipExplosion import ShipExplosion
from ExplosionManager import ExplosionManager
import GameTime
from enum import Enum
import time

#==================================================================
class State(Enum):
    INIT = 1
    GAME_OVER = 2
    WAIT_TO_START = 3
    GAME_PLAY = 4
    WAIT_FOR_NEXT_LIFE = 5
    GET_READY = 6

 
 #==================================================================
white = (255,255,255)
black = (0,0,0)
red = (255, 0, 0)

debugApp = True


 #==================================================================
class App:

    #==================================================================
    def __init__(self):
        self.state = State.INIT
        self.running = False
        self.displaySurface = None
        if debugApp:
            self.width = 768
            self.height = 480
            self.fullScreen = False
        else:
            self.width = 0
            self.height = 0
            self.fullScreen = True

        self.lives = 10
        self.score = 0

 

    #==================================================================
    def Init(self):
        pygame.mixer.pre_init(44100, -16, 2, 512)
        pygame.mixer.init()
        pygame.init()
        pygame.font.init()

        fontName = pygame.font.get_default_font()
        self.font = pygame.font.SysFont(fontName, 24, True)
        self.fontGameOver = pygame.font.SysFont(fontName, 64, True)

        fullScreen = pygame.FULLSCREEN
        if self.fullScreen == False:
            fullScreen = 0

        self.displaySurface = pygame.display.set_mode((self.width,self.height), pygame.HWSURFACE | fullScreen )
        self.width = self.displaySurface.get_width()
        self.height = self.displaySurface.get_height()

        self.running = True

        GameTime.Init( True, 1.0 / 30.0)
       
        self.bubbleManager = BubbleManager( self.width, self.height )
        self.shipManager = ShipManager( self.width, self.height, self.lives )
        self.shotManager = ShotManager( self.width, self.height )
        self.explosionManager = ExplosionManager( )

        self.explosionSFX = pygame.mixer.Sound("audio/explosion.wav")
        pygame.mixer.Sound.set_volume( self.explosionSFX, 0.20 )

        self.state = State.WAIT_TO_START
       
            
    #==================================================================   
    def Update(self):
        GameTime.Update()
        dt = GameTime.Delta()
        pygame.event.pump()
        keys = pygame.key.get_pressed()
       
        updateBubbles = False
        updateShip = False
        updateShots = False
        updateCollisions = False
        updateKeyInput = False
        updateExplosion = False

        if self.state == State.WAIT_TO_START:
            if keys[ pygame.K_SPACE ]:
                self.state = State.GET_READY
                self.stateTimer = 3.0
                self.bubbleManager.KillAll()
                self.bubbleManager.Disable()
                self.shipManager.Reset()
                self.shipManager.Enable()
                self.shotManager.KillAll()
                self.shotManager.Enable()
                self.explosionManager.KillAll()
                time.sleep( 0.25 )

        elif self.state == State.GET_READY:
            self.stateTimer = self.stateTimer - dt
            updateKeyInput = True
            updateShip = True
            updateShots = True

            if self.stateTimer <= 0.0:
                self.state = State.GAME_PLAY
                self.bubbleManager.KillAll()
                self.bubbleManager.Enable()
                

        elif self.state == State.GAME_PLAY:
            updateBubbles = True
            updateShip = True
            updateShots = True
            updateCollisions = True
            updateKeyInput = True


        elif self.state == State.WAIT_FOR_NEXT_LIFE:
            updateBubbles = True
            updateExplosion = True
            self.stateTimer = self.stateTimer - dt
            if self.stateTimer <= 0.0:
                if self.lives > 0 :
                    self.state = State.GET_READY
                    self.stateTimer = 3.0
                else:
                    self.state = State.GAME_OVER
             
        elif self.state == State.GAME_OVER:
            updateBubbles = True


        if updateKeyInput:
            if keys[ pygame.K_a ] or keys[ pygame.K_LEFT ]:
                self.shipManager.Left()
    
            if keys[ pygame.K_d ] or keys[ pygame.K_RIGHT ]:
                self.shipManager.Right()

            if keys[ pygame.K_SPACE ]:
                self.shotManager.Shoot( self.shipManager.GetPos() )

        if updateExplosion:
            self.explosionManager.update( )
        if updateBubbles:
            self.bubbleManager.update( )
        if updateShip:
            self.shipManager.update( )
        if updateShots:
            self.shotManager.update()

        if updateCollisions:

             # collision detection between the bubbles and the shots.   Kill both if they collide
            collidedWithShot = pygame.sprite.groupcollide( self.bubbleManager.GetGroup(), self.shotManager.GetGroup(), True, True )
            for b in collidedWithShot:
                self.score = self.score + 100

            # collision with the ship
            collidedWithShip = pygame.sprite.groupcollide( self.bubbleManager.GetGroup(), self.shipManager.GetGroup(), True, False )
            for b in collidedWithShip:
                pygame.mixer.Sound.play(self.explosionSFX)
                self.lives = self.lives - 1
                self.state = State.WAIT_FOR_NEXT_LIFE
                self.bubbleManager.Disable()
                self.stateTimer = 5.0
                shipRect = self.shipManager.GetPos()
                self.shipExplosion = ShipExplosion( shipRect.x, shipRect.y )
                self.explosionManager.Add( self.shipExplosion )
               
        
           
            
    #==================================================================
    def Draw(self):
        self.displaySurface.fill( black )

        drawBubbles = False
        drawShip = False
        drawShots = False
        drawGameOver = False
        drawGetReady = False
        drawScore = False
        drawLives = False
        drawPressToStart = False
        drawExplosion = False

        if self.state == State.WAIT_TO_START:
            drawPressToStart = True

        elif self.state == State.GET_READY:
            drawGetReady = True
            drawShip = True
            drawShots = True

        elif self.state == State.GAME_PLAY:
            drawBubbles = True
            drawShip = True
            drawShots = True
            drawScore = True
            drawLives = True

        elif self.state == State.GAME_OVER:
            drawBubbles = True
            drawGameOver = True
            drawScore = True
            drawLives = True

        elif self.state == State.WAIT_FOR_NEXT_LIFE:
            drawBubbles = True
            drawScore = True
            drawLives = True
            drawExplosion = True
            
       
        if drawExplosion:
            self.explosionManager.Draw( self.displaySurface )
        if drawBubbles:
            self.bubbleManager.Draw( self.displaySurface )
        if drawShip:
            self.shipManager.Draw( self.displaySurface )
        if drawShots:
            self.shotManager.Draw( self.displaySurface )

        if drawScore:
            livesString = "Score: " + str( self.score )
            scoreTextSurface = self.font.render( livesString, True, (255, 255, 255 ) )
            self.displaySurface.blit( scoreTextSurface, (100, 80) )
        
        if drawLives:
            livesString = "Lives: " + str( self.lives )
            livesTextSurface = self.font.render( livesString, True, (255, 0, 0 ) )
            self.displaySurface.blit( livesTextSurface, (100, 100) ) 

        if drawPressToStart:
            pressToStartString = "Press Space Bar to Start"
            pressToStartSurface = self.fontGameOver.render( pressToStartString, True, (255, 255, 0 ) )
            self.displaySurface.blit( pressToStartSurface, (self.width / 2 - pressToStartSurface.get_width() / 2, 
                                                            self.height / 2 - pressToStartSurface.get_height() / 2) ) 
        
        if drawGetReady:
            getReadyString = "Get Ready"
            getReadySurface = self.fontGameOver.render( getReadyString, True, (255, 255, 0 ) )
            self.displaySurface.blit( getReadySurface, (self.width / 2 - getReadySurface.get_width() / 2, 
                                                        self.height / 2 - getReadySurface.get_height() / 2) ) 

        if drawGameOver:
            gameOverString = "Game Over"
            gameOverTextSurface = self.fontGameOver.render( gameOverString, True, (0, 0, 255 ) )
            self.displaySurface.blit( gameOverTextSurface, (self.width / 2 - gameOverTextSurface.get_width() / 2, 
                                                            self.height / 2 - gameOverTextSurface.get_height() / 2) ) 
     
       
       

        pygame.display.flip()
    

    #==================================================================
    def Cleanup(self):
        pygame.font.quit()
        pygame.quit()
 
    #==================================================================
    def Exec(self):
        self.Init()

        while self.running:
            self.Update()
            self.Draw()

        self.Cleanup()
 

#==================================================================
if __name__ == "__main__" :
    theApp = App()
    theApp.Exec()
