#!/usr/bin/env python
# -*- coding: utf-8 -*-
# last mod 2012-09-20 13:49 KS

import sys
sys.path.append("../") # include folder, where the PsyTML.py file is in
import PsyTML
from PyQt4 import QtGui

def main():
    app = QtGui.QApplication(sys.argv)
    item = PsyTML.PsyTML((900, 500))
    item.viewPsyTML("./sampleHTML/item1.html")
    results = item.data
    print(results)

if __name__ == "__main__":
    main()

