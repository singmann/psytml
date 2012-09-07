import sys
import os
import PsyTML
from PyQt4 import QtGui

def main():

    app = QtGui.QApplication(sys.argv)
    file = "./sampleHTML/item1.html"
    item_html1 = "file:///" + os.path.abspath(file).replace("\\", "/")
    file = "./sampleHTML/item2.html"
    item_html2 = "file:///" + os.path.abspath(file).replace("\\", "/")
    file = "./sampleHTML/intro1.html"
    intro_html = "file:///" + os.path.abspath(file).replace("\\", "/")
    file = "./sampleHTML/demographics.html"
    demo_html = "file:///" + os.path.abspath(file).replace("\\", "/")

    intro = PsyTML.PsyTML((900, 400), (200, 200))
    intro.viewPsyTML(intro_html)
    
    item = PsyTML.PsyTML((900, 800), (200, 200))
    item.viewPsyTML(item_html1)    
    results1 = item.data
    item.viewPsyTML(item_html2)
    results2 = item.data
    
    # Note the demographics use jsVal (by Karl Seguin & Timo Haberkern) relaesed under LGPL
    # (and are in German-)
    demographics = PsyTML.PsyTML((900, 500), (200, 200))
    demographics.viewPsyTML(demo_html)    
    demographic_data = demographics.data
    
    print(results1)
    print(results2)
    print(demographic_data)
    

if __name__ == "__main__":
    main()
