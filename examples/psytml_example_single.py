import PsyTML
import sys
import os
from PyQt4 import QtGui

def main():
    app = QtGui.QApplication(sys.argv)
    file = "./sampleHTML/item1.html"
    html = "file:///" + os.path.abspath(file).replace("\\", "/")
    item = PsyTML.PsyTML((900, 500), (200, 200))
    item.viewPsyTML(html)
    results = item.data
    print(results)

if __name__ == "__main__":
    main()
