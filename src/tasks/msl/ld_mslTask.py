# -*- coding: utf-8 -*-
# MSL task

from psychopy import visual, core, event, logging
from ld_utils import createWindow, createOutputFile
from ld_messages import taskMessage1, taskMessage2, waitforScanMessage
from numpy import inf
from ld_mslMenu import getParamMenu
import numpy as np
import sys

#Menu
infos = getParamMenu()

#Log
logging.addLevel(logging.EXP+1,'StartExp')
logging.addLevel(logging.EXP+2,'StartPerformance')
logging.addLevel(logging.EXP+4,'StartRest')
logDat = logging.LogFile(createOutputFile(),
    filemode='w',  # if you set this to 'a' it will append instead of overwriting
    level=logging.EXP+1)  # errors, data and warnings will be sent to this logfile

#Create Window @TODO Check multiple monitor and flip
currWindow = createWindow()

# Presentation - wait for TRIGGER
taskStim1 = visual.TextStim(currWindow, text=taskMessage1[infos['language']], color='gold',wrapWidth=100, pos=(0,.5))
taskStim2 = visual.TextStim(currWindow, text=taskMessage2[infos['language']], color='gold',wrapWidth=100, pos=(0,.3))
taskStim3 = visual.TextStim(currWindow, text=infos['seq'], color='gold',wrapWidth=100, pos=(0,0))
waitStim = visual.TextStim(currWindow, text=waitforScanMessage[infos['language']], color='gold',wrapWidth=100, pos=(0,-.7))

#Draw messages
taskStim1.draw()
taskStim2.draw()
taskStim3.draw()
waitStim.draw()
currWindow.flip()

#Reformat SEQ
infos['seq'] = infos['seq'].replace(' - ','')

# Create Cross before starting the experiment 
cross = visual.ShapeStim(currWindow, units='cm',
    vertices=((0, -2), (0, 2), (0,0), (-2,0), (2, 0)),
    lineWidth=900,
    closeShape=False,
    lineColor='red')

# Wait for trigger
out = event.waitKeys(maxWait=inf, keyList=['5'], timeStamped=True)

# Reset Clock
globalClock = core.Clock()  
logging.setDefaultClock(globalClock)

#First RED Cross
currWindow.logOnFlip('', level=logging.EXP+1)
cross.draw()
currWindow.flip()
core.wait(infos['durRest'])

# Read Keys while RED Cross
if 'escape' in event.getKeys(keyList=['1','2','3','4','escape'],timeStamped=globalClock):
    logging.flush()
    core.quit()

mean = []
correctSeq = []
    
for nblock in range(0,infos['nbBlocks']):
    
    #StartPerformance
    currWindow.logOnFlip(str(nblock), level=logging.EXP+2)
    cross.setLineColor('green')
    cross.draw()
    currWindow.flip()
    
    # Read nbKeys = 1, 2, 3, 4 or escape
    out = []
    for nbKeys in range(0,infos['nbKeys']):
        out.append(event.waitKeys(maxWait=inf, keyList=['1','2','3','4','escape'],timeStamped=globalClock))
        
    # Check if escape have been pressed
    if [item for item in out if 'escape' in item[0]]:
        logging.flush()
        core.quit()
    
    logging.data('before')
    out = [i[0] for i in out]
    
    rep = [i[0] for i in out]
    rep = ''.join(rep)
    
    timing = [i[1] for i in out]
    
    mean.append(np.mean(np.diff(timing)))
    correctSeq.append(rep.count(infos['seq']))
    
    print correctSeq
    print mean
    logging.data('after')
    
    #StartRest
    currWindow.logOnFlip(str(nblock), level=logging.EXP+4)
    cross.setLineColor('red')
    cross.draw()
    currWindow.flip()
    core.wait(infos['durRest'])
    
    # Read Keys while RED Cross
    if 'escape' in event.getKeys(keyList=['1','2','3','4','escape'], timeStamped=globalClock):
        logging.flush()
        core.quit()
    
currWindow.close()