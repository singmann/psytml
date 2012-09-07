# version 1.0: 7th September 2012
# Henrik Singmann with help from ekhumoror (http://stackoverflow.com/users/984421/ekhumoro)
# License: GPL v3

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

