# ABore - 6 Avril 2017
# CRIUGM
# -*- coding: utf-8 -*-

from psychopy import gui  #fetch default gui handler (qt if available)
from ld_config import arrow_seqA, arrow_seqB, arrow_nbBlocks, arrow_nbKeys, arrow_durRest, flipMonitor, fullScreen
import os
import Tkinter

def getParamMenu():
    # create a DlgFromDict
    info = {'Observer':['ABoutin', 'EGabitov'],
        'seq':[' - '.join(map(str, arrow_seqA)), ' - '.join(map(str, arrow_seqB))],
        'nbBlocks':arrow_nbBlocks,
        'nbKeys':arrow_nbKeys,
        'durRest':arrow_durRest,
        'language':['French', 'English'],
        'flipMonitor':flipMonitor,
        'FullScreen':fullScreen}
    
    infoDlg = gui.DlgFromDict(dictionary=info, title='Stim Experiment - v0.1',
        order=['Observer','language','flipMonitor','FullScreen','seq','nbBlocks','nbKeys','durRest'],
        tip={'Observer': 'trained visual observer, initials', 'durRest': 'seconds'})

    if infoDlg.OK:  # this will be True (user hit OK) or False (cancelled)
        info['language'] = checkLanguage(info['language'])
        return info

def checkLanguage(currLanguage):
    if currLanguage == 'French': 
        return 0
    elif currLanguage == 'English':
        return 1
    
