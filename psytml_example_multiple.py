import sys
import os
from urllib import unquote_plus

from PyQt4 import QtCore, QtGui, QtWebKit

class MyWebPage(QtWebKit.QWebPage):
    formSubmitted = QtCore.pyqtSignal(object)

    def acceptNavigationRequest(self, frame, req, nav_type):
        if nav_type == QtWebKit.QWebPage.NavigationTypeFormSubmitted:
            elements = {}
            for key, value in req.url().encodedQueryItems():
                key = unquote_plus(bytes(key)).decode('utf8')
                value = unquote_plus(bytes(value)).decode('utf8')
                elements[key] = value
            self.formSubmitted.emit(elements)
        return super(MyWebPage, self).acceptNavigationRequest(frame, req, nav_type)

class PsyTML(QtGui.QDialog):
    def __init__(self, size, position):
        super(PsyTML, self).__init__()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.resize(size[0], size[1])
        self.move(position[0], position[1])
        self.data = {}
        self.view = QtWebKit.QWebView(self)
        layout = QtGui.QVBoxLayout(self)
        layout.addWidget(self.view)
        layout.setContentsMargins(0, 0, 0, 0)
        self.view.setPage(MyWebPage())
        self.view.page().formSubmitted.connect(self.handleFormSubmitted)

    def viewPsyTML(self, html):
        self.view.setUrl(QtCore.QUrl(html))
        self.exec_()

    def handleFormSubmitted(self, elements):
        self.data = elements
        self.accept()


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

    intro = PsyTML((900, 400), (200, 200))
    intro.viewPsyTML(intro_html)
    
    item = PsyTML((900, 800), (200, 200))
    item.viewPsyTML(item_html1)    
    results1 = item.data
    item.viewPsyTML(item_html2)
    results2 = item.data
    
    # Note the demographics use jsVal (by Karl Seguin & Timo Haberkern) relaesed under LGPL-
    demographics = PsyTML((900, 500), (200, 200))
    demographics.viewPsyTML(demo_html)    
    demographic_data = demographics.data
    
    print(results1)
    print(results2)
    print(demographic_data)
    

if __name__ == "__main__":
    main()
