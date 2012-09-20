#!/usr/bin/env python
# -*- coding: utf-8 -*-
# last mod 2012-09-20 22:12 KS
import sys
sys.path.append("../") # include folder, where the psytml.py file is in
import functools
import psytml
from PyQt4 import QtGui

def main():

    app = QtGui.QApplication(sys.argv)

    # create function with default size and position
    show_form_defaults = functools.partial(psytml.show_form,
            size= (900, 600), position=(0, 0))

    psytml.show_form("./sampleHTML/intro1.html", (900, 400), None)
    results1 = show_form_defaults("./sampleHTML/item1.html")
    results2 = show_form_defaults("./sampleHTML/item2.html")

    # Note the demographics use jsVal (by Karl Seguin & Timo Haberkern)
    # released under LGPL (and are in German)
    demographics = psytml.show_form(
            filename="./sampleHTML/demographics.html",
            size=(900, 500),
            position=(200, 200))

    print(results1)
    print(results2)
    print(demographics)

if __name__ == "__main__":
    main()

