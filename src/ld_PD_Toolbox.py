# ABore - 6 Avril 2017
# CRIUGM
# -*- coding: utf-8 -*-

import tkinter
import sys
import os
    
rawFolder = os.getcwd() + os.path.sep

def createMSLTask(topMenu):
    mslTask = tkinter.Button(topMenu, text ="MSL", command=runMSL)
    mslTask.grid(column=0,row=0)

def createRhythmTask(topMenu):
    rhythmTask = tkinter.Button(topMenu, text ="Rhythm", command=runRhythm)
    rhythmTask.grid(column=1,row=0)
    
def createArrowTask(topMenu):
    arrowTask = tkinter.Button(topMenu, text ="Arrow", command=runArrow)
    arrowTask.grid(column=2,row=0)

def createCongruencyTask(topMenu):
    fofixTask = tkinter.Button(topMenu, text ="Congruency", command=runCongruency)
    fofixTask.grid(column=3,row=0)    
    
def createFoFixTask(topMenu):
    fofixTask = tkinter.Button(topMenu, text ="FoFix", command=runFoFix)
    fofixTask.grid(column=4,row=0)
    
def runMSL():
    os.chdir(rawFolder + 'tasks/msl')
    os.system('python ld_mslMenu.py')

def runRhythm():
    os.chdir(rawFolder + 'tasks/rhythm')
    os.system('python ld_rhythmTask.py')

def runArrow():
    os.chdir(rawFolder + 'tasks/arrow')
    os.system('python ld_arrowTask.py')

def runCongruency():
    os.chdir(rawFolder + 'tasks/congruency')
    os.system('python ld_congruencyTask.py')
    
def runFoFix():
    print 'FoFix'
    
#Menu
toolbox = tkinter.Tk()
toolbox.grid()
toolbox.title('Toolbox - Parkinson')
createMSLTask(toolbox)
createRhythmTask(toolbox)
createArrowTask(toolbox)
createCongruencyTask(toolbox)
createFoFixTask(toolbox)
toolbox.mainloop()
