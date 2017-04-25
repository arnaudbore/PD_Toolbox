import os

rawFolder = os.getcwd() + os.path.sep

#### Pictures
standford_fr = os.path.join(rawFolder,'..','..','stimulis','StanfordSleepinessScale_fr.png')
standford_en = os.path.join(rawFolder,'..','..','stimulis','StanfordSleepinessScale_en.png')
handPicture = os.path.join(rawFolder,'..','..','stimulis','Hand.png')

#### WINDOW
fullScreen = False
flipMonitor = False

#### TASKS
### Congruency Parameters
#Visu
congruency_circleLineColor = 'white'
congruency_circleFillColor = 'black'
congruency_circleRadius = .2
congruency_congruentColors = ['gold','blueviolet']

#Experience
congruency_jitter = [2, 3]
congruency_durRest = 2
###


### MSL Parameters
#Visu

#Experience
msl_nbBlocks = 2
msl_nbKeys = 10
msl_seqA = [1,4,2,3,1]
msl_seqB = [4,1,3,2,4]
msl_nbSeqIntro = 3
msl_durRest = 2
###

### Rhythm Parameters
#Visu

#Experience
rhythm_nbBlocks = 2
rhythm_durRest = 2
rhythm_freq = 2
rhythm_shortRest = 2
rhythm_halfBlockDuration=45
###

### Arrow Parameters
#Visu
arrow_circleColor='red'
arrow_circleRadius=1

#Experience
arrow_nbBlocks = 2
arrow_nbKeys = 10
arrow_seqA = [0,2,1,0,3,4,0,1,3,2,4] # Seq between 0 and 4
arrow_seqB = [4,1,3,2,4]
arrow_durRest = 2

arrow_sizePenta = 4.8 #cm
arrow_flipArrow = 0 #72 or 0
###
