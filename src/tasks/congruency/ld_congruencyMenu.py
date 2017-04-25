# ABore - 6 Avril 2017
# CRIUGM
# -*- coding: utf-8 -*-

from psychopy import gui  #fetch default gui handler (qt if available)
from ld_config import congruency_durRest
import os
import tkinter
from tkFileDialog import askopenfilename
from ld_utils import readDesign

def getParamMenu():
    # create a DlgFromDict
    info = {'Observer':['ABoutin', 'EGabitov'],
        'durRest':congruency_durRest,
        'language':['French', 'English'],
        'flipMonitor':False,
        'FullScreen':False}
    
    infoDlg = gui.DlgFromDict(dictionary=info, title='Stim Experiment - v0.1',
        order=['Observer','language','flipMonitor','FullScreen','durRest'],
        tip={'Observer': 'trained visual observer, initials', 'durRest': 'seconds'})

    
    tkinter.Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
    info['design'] = readDesign(filename)
    
    if infoDlg.OK:  # this will be True (user hit OK) or False (cancelled)
        info['language'] = checkLanguage(info['language'])
        return info


    
def checkLanguage(currLanguage):
    if currLanguage == 'French': 
        return 0
    elif currLanguage == 'English':
        return 1

    