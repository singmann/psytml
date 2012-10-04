#!/usr/bin/env python
# -*- coding: utf-8 -*-
# last mod 2012-10-02 10:20 KS

"""
example that shows how to use PsyTML and PsychoPy together.

.. note:
    Note, you want to change the number, name, and size of the screen before
    running this.

"""

import sys # needed only for initializing the QT App
sys.path.append("../../") # include folder, where the psytml.py file is in
import functools # set default arguments in function

## import all libraries that are needed
from psychopy import visual, event, core # needed for PsychoPy functionality
from PyQt4 import QtGui # needed for initializing Qt
from numpy import random as rnd # needed for randomizing the trial order

import psytml # needed to present the HTML pages
import helper #needed for getting the id, condition and writing data.

## Parameters for the experiment
EXP_NAME = "example1"
BG_COLOR = "#c0c0c0"
DATA_FOLDER = "data"
PATH_ID_FILE = "." # set the (preferably network) path to the file
                   # containing the Ids and Conditions.

# empty list that will collect the data per trial (as Python dict)
data = []

## Get Participant Number and initialize everything
id_, condition = helper.getId(PATH_ID_FILE)

app = QtGui.QApplication(sys.argv) # initialize QT App
# Extract screen width and height with QtGui. You can also set this manually,
# by assigning values to width and height
screen_size = QtGui.QApplication.desktop().size()
width, height = screen_size.width(), screen_size.height()

# initialize Windows and Mouse object from PsychoPy
win = visual.Window((width, height), monitor='testMonitor', fullscr=False,
        allowGUI=False, units='norm', color=BG_COLOR, winType='pyglet')
mouse = event.Mouse(win=win, visible=True)

## Create and randomize stimuli
# create items based on condition:
if (condition == "causal"):
    items = ["../sampleHTML/item_c_1.html", "../sampleHTML/item_c_2.html"]
if (condition == "noncausal"):
    items = ["../sampleHTML/item_nc_1.html", "../sampleHTML/item_nc_2.html"]
rnd.shuffle(items)  #shuffle items

# initialize screen and mouse for the presentation of stimuli
mouse.setVisible(True)
win.flip()

# set default size and position with functools to simplify repeated use
show_form_intro = functools.partial(psytml.show_form, size=(900, 700),
        position=(0, 0)) # in contrast to PsychoPy Position starts in the
                         # upper left corner. position=None to center form
show_form_intro("../sampleHTML/intro1.html")

## Show some PsychoPy stuff (copied from aperture demo)
mouse.setVisible(False)
gabor1 = visual.PatchStim(win, mask='circle', pos=[0.2, 0.2],
    sf=4, size=.4,
    color=[0.5,-0.5,1])
gabor2 = visual.PatchStim(win, mask='circle', pos=[-0.2, -0.2],
    sf=4, size=.4,
    color=[-0.5,-0.5,-1])
text = visual.TextStim(win, "hit 'q' to continue", pos=(0, -0.5))

aperture = visual.Aperture(win, size=.5,pos=[0.16, 0.16], shape='square')
select = "gabor1"
while True:
    if select == "gabor1":
        aperture.enable() #actually is enabled by default when created
        gabor1.draw()
        select = "gabor2"
    elif select == "gabor2":
        aperture.disable() #drawing from here ignores aperture
        gabor2.draw()
        select = "gabor1"
    text.draw()
    win.flip()
    core.wait(0.1)
    if "q" in event.getKeys():
        break

# make the psychopy window empty and show mouse again
mouse.setVisible(True)
win.flip()
win.flip() # on some graphics cards win.flip must be called twice to get an
           # empty screen

## Present html trials with psytml
for trial_num, item in enumerate(items):
    data_trial = psytml.show_form(item, (900, 700), None)
    data_trial.update({"id":id_, "condition":condition, "trial": trial_num+1})        # here you could add other information that should be written to each trial.
    data.append(data_trial) # add current trial to the data list.

## Writing the trial data:
data_header = ["id", "condition", "trial", "content", "causal", "power", "resp"]    # The header needs to match the keys in the dictionary stored in data
# the header will be written as the first line in the data file (as long as
# print_header is True when calling writeTrials)
# when called like this a file with the same name will be overwritten
helper.writeTrials(header=data_header, list=data, path=DATA_FOLDER,
        expName=EXP_NAME, id=id_)

## Get demographic data and show final screens
# Note the demographics use jsVal (by Karl Seguin & Timo Haberkern) relaesed
# under LGPL
demographics = show_form_intro("../sampleHTML/demographics.html")
comments = show_form_intro("../sampleHTML/end.html")

## Write demographic data and comments
demographics_header = ["sex", "age", "education", "glasses1", "glasses2"]
helper.writeDemographics(demographics_header, demographics,
        DATA_FOLDER, EXP_NAME, id_, condition, sep=";")
helper.writeComments(comments, DATA_FOLDER, id_, EXP_NAME)

## print all data to the console
print(data)
print(demographics)
print(comments)

## show final screen with password
show_form_intro("../sampleHTML/final.html")

## close the program.
win.close()
core.quit()

