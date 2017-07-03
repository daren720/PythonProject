

from datetime import datetime
from datetime import timedelta


#==================================================================
def Init( enforcefpsParam = False, maxfpsParam = 0.0 ):
    global startTime
    global lastTime
    global deltaTime
    global currentTime
    global enforcefps
    global maxfps
    
    enforcefps = enforcefpsParam
    maxfps = maxfpsParam

    startTime = datetime.now()
    lastTime = Time()
    deltaTime = 0.0
    currentTime = startTime
       
#==================================================================
def Time():
    global startTime

    dt = datetime.now() -  startTime
    ms = (dt.days * 24 * 60 * 60 + dt.seconds) * 1000 + dt.microseconds / 1000.0
    s = ms * 0.001
    return s

#==================================================================
def Update():
    global lastTime
    global deltaTime
    global currentTime

    currentTime = Time()
    deltaTime = currentTime - lastTime
    if ( enforcefps and deltaTime > maxfps):
        deltaTime = maxfps

    lastTime = currentTime

    #==================================================================
def Delta():
    global deltaTime

    return deltaTime
    



