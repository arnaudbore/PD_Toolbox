from __future__ import division

from psychopy import visual, core, event, logging
from ld_utils import createWindow, createOutputFile, getCircleColor
from ld_config import congruency_circleFillColor, congruency_circleRadius, congruency_circleLineColor, congruency_jitter
from ld_congruencyMenu import getParamMenu
from ld_messages import readyMessage
import numpy as np
from random import randint, uniform


#Menu
infos = getParamMenu()

#Log
logging.addLevel(logging.EXP+1,'StartExp')
logging.addLevel(logging.EXP+2,'StartPerformance')
logging.addLevel(logging.EXP+4,'StartRest')
logging.addLevel(logging.EXP+5,'Key')
logging.addLevel(logging.EXP+6,'Answer')
logDat = logging.LogFile(createOutputFile(),
    filemode='w',  # if you set this to 'a' it will append instead of overwriting
    level=logging.EXP+1)  # errors, data and warnings will be sent to this logfile

#Create Window @TODO Check multiple monitor and flip
currWindow = createWindow()

#Create Mouse object but keep it invisible
m = event.Mouse(visible=False, win=currWindow)

#Create left circle
leftCircle = visual.Circle(currWindow, fillColor=congruency_circleFillColor, lineColor=congruency_circleLineColor, radius=congruency_circleRadius, edges=32)
leftCircle.pos = (-.5,1/6)

#Create right circle
rightCircle = visual.Circle(currWindow, fillColor=congruency_circleFillColor, lineColor=congruency_circleLineColor, radius=congruency_circleRadius, edges=32)
rightCircle.pos = (.5,1/6)

#Create grey line
gLine = visual.Line(currWindow, start=(-1, -2/3), end=(1, -2/3), lineColor='grey')

#Create Right Box
rightAnswer = visual.TextStim(currWindow, text='Right', pos=(.5, -5/6), color='gold')
rightAnswer.setUnits = 'pixels'
rightBox = visual.Rect(currWindow, width=rightAnswer.width/currWindow.size[0], height=rightAnswer.height+.01, pos=(.5, -5/6), lineColor='white')

#Create Left Box
leftAnswer = visual.TextStim(currWindow, text='Left', pos=(-.5, -5/6), color='gold')
leftAnswer.setUnits = 'pixels'
leftBox = visual.Rect(currWindow, width=leftAnswer.width/currWindow.size[0] , height=leftAnswer.height+.01, pos=(-.5, -5/6), lineColor='white')

waitStim = visual.TextStim(currWindow, text=readyMessage[infos['language']], color='gold',wrapWidth=100, pos=(0,-.7))
waitStim.draw()
currWindow.flip()

out = event.waitKeys(maxWait=np.inf, keyList=['5'], timeStamped=True)

#Reset Clock
globalClock = core.Clock()  
logging.setDefaultClock(globalClock)

# Draw everything 
leftBox.draw()
rightBox.draw()
leftCircle.draw()
rightCircle.draw()
gLine.draw()
leftAnswer.draw()
rightAnswer.draw()
currWindow.flip(clearBuffer=False)

core.wait(infos['durRest'])

nBlock = 0
nextBlock = True
for nKey in infos['design']:
    if nKey[0]>1:
        currWindow.logOnFlip(str(nBlock), level=logging.EXP+4)
        nBlock += 1
        leftCircle.fillColor = congruency_circleFillColor
        rightCircle.fillColor = congruency_circleFillColor
        leftCircle.draw()
        rightCircle.draw()
        currWindow.flip(clearBuffer=False)
        nextBlock = True
        core.wait(infos['durRest'])
    else:
        leftCircle.fillColor, rightCircle.fillColor = getCircleColor(nKey)
        #StartPerformance
        if nextBlock:
            currWindow.logOnFlip(str(nBlock), level=logging.EXP+2)
            currWindow.logOnFlip(str(nKey), level=logging.EXP+5)
            nextBlock = False
            
        leftCircle.draw()
        rightCircle.draw()
        currWindow.flip(clearBuffer=False)
        next = False
        while not next:
            if m.isPressedIn(leftBox):
                currWindow.logOnFlip('left', level=logging.EXP+6)
                next=True
            if m.isPressedIn(rightBox):
                currWindow.logOnFlip('right', level=logging.EXP+6)
                next=True
                
        leftCircle.fillColor = congruency_circleFillColor
        rightCircle.fillColor = congruency_circleFillColor
        leftCircle.draw()
        rightCircle.draw()
        currWindow.flip(clearBuffer=False)
        core.wait(uniform(congruency_jitter[0],congruency_jitter[1]))

        
leftCircle.fillColor = congruency_circleFillColor
rightCircle.fillColor = congruency_circleFillColor
leftCircle.draw()
rightCircle.draw()
currWindow.flip(clearBuffer=False)
core.wait(infos['durRest'])    

currWindow.close()


