import PsyTML
import sys
from PyQt4 import QtGui

def main():
    app = QtGui.QApplication(sys.argv)
    item = PsyTML.PsyTML((900, 500))
    item.viewPsyTML("./sampleHTML/item1.html")
    results = item.data
    print(results)

if __name__ == "__main__":
    main()
