#!/usr/bin/env python
# -*- coding: utf-8 -*-

## Note, you want to change the number, name, and size of the screen before running this!

## import all libraries that are needed
from psychopy import visual, event, core, monitors          # needed for PsychoPy functionality
import os       # needed for constructing well formed paths to HTML files
from PyQt4 import QtGui         # needed for initializing Qt
import sys      # needed only for initializing the QT App
from numpy import random as rnd     # needed for randomizing the trial order
import PsyTML       # needed to present the HTML pages
import helper       #needed for getting the id, condition and writing data.

## Parameters for the experiment
expName = "example1"
bgColor = 	"#c0c0c0"
data_folder = "data"

data = []       # empty list that will collect the data per trial (as Python dictionnaries)

pathToIdFile = "."      #set the (preferably network) path to the file containing the Ids and Conditions.

## Get Participant Number and initialize everything
(id, condition) = helper.getId(pathToIdFile)          # get participant number and condition

app = QtGui.QApplication(sys.argv)      # initialize QT App

# initialize Windows and Mouse object from PsychoPy
myWin = visual.Window((1024,768), monitor='testMonitor', fullscr=False, allowGUI=False, units ='pix', color = bgColor, winType='pyglet')
#myWin = visual.Window((1920,1080), monitor='sozPsyMon2', fullscr=False, allowGUI=False, units ='pix', color = bgColor, winType='pyglet', screen = 1)
myMouse = event.Mouse(win = myWin, visible = True)

# initialize screen for PsyTML (the start field is necessary, otherwise the first html page will not be on bgColor background when screen size is fullscr)
myMouse.setVisible(True)
PsyTML.Start(id, condition)
# if you don't want to present the condition: PsyTML.Start(myWin, myMouse, id)

## Create and randomize stimuli
# create items based on condition:
if (condition == "causal"):
    items = ["html/item_c_1.html", "html/item_c_2.html"]
if (condition == "noncausal"):
    items = ["html/item_nc_1.html", "html/item_nc_2.html"]
rnd.shuffle(items)  #shuffle items

## initialize screen and mouse for the presentation of stimuli
myMouse.setVisible(True)
myWin.flip()

## present introduction (if there are more screens, call intro.viewPsyTML() multiple times with the correct argument)
intro = PsyTML.PsyTML(size = (900, 800), position = (0, 0))       #in contrast to PsychoPy Position starts in the upper left corner.
# intro = PsyTML.PsyTML(size = (900, 800) # uncomment this line and comment the line above to center the instruction and password.
intro.viewPsyTML("html/intro1.html")

## Present trials
item_win = PsyTML.PsyTML((900, 800))        # create PsyTML object for the items, if position is the default or True it is centered.
for trial_num, item in enumerate(items):
    item_win.viewPsyTML(item)       # present the trial
    tmp = item_win.data        # read dictionary from trial
    tmp.update({"id":id, "condition":condition, "trial": trial_num+1})        # here you could add other information that should be written to each trial.
    data.append(tmp)        # add current trial to the data list.

## Writing the trial data:
data_header = ["id", "condition", "trial", "content", "causal", "power", "resp"]    # The header needs to match the keys in the dictionary stored in data
# the header will be written as the first line in the data file (as long as print_header is True when calling writeTrials)
helper.writeTrials(header = data_header, list = data, path = data_folder, expName = expName, id = id)   #when called like this a file with the same name will be overwritten

## Get demographic data and show final screens
#Note the demographics use jsVal (by Karl Seguin & Timo Haberkern) relaesed under LGPL
demographics = PsyTML.PsyTML((900, 700))    # html is centered on screen.
demographics.viewPsyTML("html/demographics.html")    
demographic_data = demographics.data
demographics.viewPsyTML("html/end.html")
comments = demographics.data

## Write demographc data and comments
demographics_header = ["sex", "age", "education", "glasses1", "glasses2"]
helper.writeDemographics(demographics_header, demographic_data, data_folder, expName, id, condition, sep = ";")
helper.writeComments(comments, data_folder, id, expName)

## print all data to the console
print(data)
print(demographic_data)
print(comments)

## show final screen with password
intro.viewPsyTML("html/final.html")

## close the program.
myWin.close()
core.quit()

