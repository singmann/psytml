#!/usr/bin/env python
# -*- coding: utf-8 -*-
# last mod 2012-09-20 13:49 KS

import sys
sys.path.append("../") # include folder, where the psytml.py file is in
import psytml
from PyQt4 import QtGui

app = QtGui.QApplication(sys.argv)
results = psytml.show_form("./sampleHTML/item_nc_1.html", size=(900, 600))
print(results)
resp = int(results["resp"])

if resp < 0:
    print("unsatisfied")
else:
    print("satisfied or neutral")

