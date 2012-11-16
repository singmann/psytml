#!/usr/bin/env python
# -*- coding: utf-8 -*-
# last mod 2012-11-08 17:47 HS

"""
Example for how to use "deg" and "cm" units from psychopy to use with psytml.

Positioning of the windows is a bit erratic to demonstrate how to use the
units.

"""

import sys
sys.path.append("..") # include folder, where the psytml.py file is in
from psytml_psychopy import show_form
from psychopy import monitors
from PyQt4 import QtGui

mon = monitors.Monitor('testMonitor')
mon.setDistance(114)
app = QtGui.QApplication(sys.argv)
# norm
results = show_form("./sampleHTML/item_nc_1.html", size=(1.5, 0.75),
                    position=(0.1, 0.1), units="norm", monitor=mon)
print(results)
# cm
results = show_form("./sampleHTML/item_nc_1.html", size=(25, 15),
                    position=(1, -1), units="cm", monitor=mon)
print(results)
# deg
results = show_form("./sampleHTML/item_nc_1.html", size=(15, 5),
                    position=(2, -2), units="deg", monitor=mon)
print(results)
resp = int(results["resp"])

if resp < 0:
    print("unsatisfied")
else:
    print("satisfied or neutral")
