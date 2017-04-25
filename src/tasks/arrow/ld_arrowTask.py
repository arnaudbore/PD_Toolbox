from __future__ import division

from psychopy import visual, core, event, logging
from ld_utils import createWindow, getArrowVertices, createOutputFile
from ld_config import arrow_sizePenta, arrow_flipArrow, arrow_circleColor, arrow_circleRadius
from ld_arrowMenu import getParamMenu
from ld_messages import readyMessage
import numpy as np
from random import randint

#Menu
infos = getParamMenu()

#Log
logging.addLevel(logging.EXP+1,'StartExp')
logging.addLevel(logging.EXP+2,'StartPerformance')
logging.addLevel(logging.EXP+4,'StartRest')
logging.addLevel(logging.EXP+5,'Key')
logDat = logging.LogFile(createOutputFile(),
    filemode='w',  # if you set this to 'a' it will append instead of overwriting
    level=logging.EXP+1)  # errors, data and warnings will be sent to this logfile

#Create Window @TODO Check multiple monitor and flip
currWindow = createWindow()

#Create Mouse object but keep it invisible
m = event.Mouse(visible=False, win=currWindow)

#Create a template pentagon to get vertices
# Param:
#   - sizePenta in cm
penta = visual.Polygon(currWindow, edges=5, radius=arrow_sizePenta, units='cm')

#Create an arrow using penta vertices 
# Param:
#   - fillColor = 'white' - should be a variable
arrow = visual.ShapeStim(currWindow, vertices=getArrowVertices(penta.vertices), fillColor='white', interpolate=True,units='cm')
arrow.ori = arrow_flipArrow

#Create a circle 
circle = visual.Circle(currWindow, fillColor=arrow_circleColor, lineColor=arrow_circleColor, radius=arrow_circleRadius, units='cm', edges=32)


#Create Red Cross for rest periods
cross = visual.ShapeStim(currWindow, units='cm',
    vertices=((0, -2), (0, 2), (0,0), (-2,0), (2, 0)),
    lineWidth=900,
    closeShape=False,
    lineColor='red')

waitStim = visual.TextStim(currWindow, text=readyMessage[infos['language']], color='gold',wrapWidth=100, pos=(0,-.7))
waitStim.draw()
currWindow.flip()

#Reformat SEQ
infos['seq'] = infos['seq'].replace(' - ','')

# Wait for trigger
out = event.waitKeys(maxWait=np.inf, keyList=['5'], timeStamped=True)

# Reset Clock
globalClock = core.Clock()  
logging.setDefaultClock(globalClock)

#First RED Cross
currWindow.logOnFlip('', level=logging.EXP+1)
cross.draw()
currWindow.flip()
core.wait(infos['durRest'])

circleIndex = randint(0,len(infos['seq'])-1)
next = False

for nBlock in range(0,infos['nbBlocks']):
    #StartPerformance
    currWindow.logOnFlip(str(nBlock), level=logging.EXP+2)
    arrow.draw()
    currWindow.flip()
    
    for nbKeys in range(0,infos['nbKeys']):
        # New Position
        currWindow.logOnFlip(infos['seq'][circleIndex], level=logging.EXP+5)
        circle.setPos(penta.vertices[int(infos['seq'][circleIndex])])
        arrow.draw()
        circle.draw()
        currWindow.flip()
        next = False
        while not next:
            if m.isPressedIn(circle):
                next = True
                circleIndex += 1
                if circleIndex>=len(infos['seq']):
                    circleIndex=0
 
    currWindow.logOnFlip(str(nBlock), level=logging.EXP+4)
    cross.draw()
    currWindow.flip()
    core.wait(infos['durRest'])
