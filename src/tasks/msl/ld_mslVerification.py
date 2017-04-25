# -*- coding: utf-8 -*-

from psychopy import visual, core, event
from ld_utils import createWindow
from ld_config import handPicture
from ld_messages import readyMessage, pressMessage
from numpy import inf

currWindow = createWindow()

# Presentation
textstim1 = visual.TextStim(currWindow, text=readyMessage[0], color='gold',wrapWidth=100, pos=(0,-.8))
textstim1.draw()

# Show Hand
handPicture = visual.ImageStim(currWindow, image=handPicture, interpolate=True, pos=(0,0.1))
handPicture.setSize(handPicture.size*.7/(max(handPicture.size)/2))
handPicture.draw()

currWindow.flip()

# Wait for TTL (or keyboard input) before starting
out = event.waitKeys(maxWait=inf, keyList=['5'], modifiers=False, timeStamped=True)

for nButton in range(1,5):
    textstim1 = visual.TextStim(currWindow, text=pressMessage[0] + str(nButton), color='gold',wrapWidth=100)
    textstim1.draw()
    currWindow.flip()
    out = event.waitKeys(maxWait=inf, keyList=[str(nButton)], modifiers=False, timeStamped=True)
    if out[0] == str(nButton):
        success = 1;

    success = 0;
    
currWindow.close()