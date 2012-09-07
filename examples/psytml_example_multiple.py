import sys
import os
import PsyTML
from PyQt4 import QtGui

def main():

    app = QtGui.QApplication(sys.argv)

    intro = PsyTML.PsyTML((900, 400), True)
    intro.viewPsyTML("./sampleHTML/intro1.html")
    
    item = PsyTML.PsyTML((900, 800), (0, 0))
    item.viewPsyTML("./sampleHTML/item1.html")    
    results1 = item.data
    item.viewPsyTML("./sampleHTML/item2.html")
    results2 = item.data
    
    # Note the demographics use jsVal (by Karl Seguin & Timo Haberkern) relaesed under LGPL
    # (and are in German-)
    demographics = PsyTML.PsyTML((900, 500), (200, 200))
    demographics.viewPsyTML("./sampleHTML/demographics.html")    
    demographic_data = demographics.data
    
    print(results1)
    print(results2)
    print(demographic_data)
    

if __name__ == "__main__":
    main()
