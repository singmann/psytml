import sys
import os
from urllib import unquote_plus

from PyQt4 import QtCore, QtGui, QtWebKit

class MyWebPage(QtWebKit.QWebPage):
    formSubmitted = QtCore.pyqtSignal(QtCore.QUrl)

    def acceptNavigationRequest(self, frame, req, nav_type):
        if nav_type == QtWebKit.QWebPage.NavigationTypeFormSubmitted:
            self.formSubmitted.emit(req.url())
        return super(MyWebPage, self).acceptNavigationRequest(frame, req, nav_type)

class PsyTML(QtGui.QWidget):
    def __init__(self, html, elements, size, position):
        super(PsyTML, self).__init__()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.resize(size[0], size[1])
        self.move(position[0], position[1])
        QtWebKit.QWebSettings.globalSettings().setAttribute(QtWebKit.QWebSettings.PluginsEnabled, True)
        view = QtWebKit.QWebView(self)
        layout = QtGui.QVBoxLayout(self)
        layout.addWidget(view)
        layout.setContentsMargins(0, 0, 0, 0)
        view.setPage(MyWebPage())
        view.setUrl(QtCore.QUrl(html))
        view.page().formSubmitted.connect(self.handleFormSubmitted)
        self.elements = elements

    def handleFormSubmitted(self, url):
        elements = self.elements
        self.close()
        for key, value in url.encodedQueryItems():
            key = unquote_plus(bytes(key)).decode('utf8')
            value = unquote_plus(bytes(value)).decode('utf8')
            elements[key] = value
        # do stuff with elements...
        # for item in elements.iteritems():
            # print '"%s" = "%s"' % item
        #QtGui.qApp.quit()
        QtGui.qApp.closeAllWindows()
    
    def returnDict(self):
        return(self.elements)

def main():
    results = {}
    app = QtGui.QApplication(sys.argv)
    file = "./sampleHTML/item1.html"
    html = "file:///" + os.path.abspath(file).replace("\\", "/")
    item = PsyTML(html, results, (900, 500), (200, 200))
    item.show()
    app.exec_()
    print(results)
    print(item.returnDict())

if __name__ == "__main__":
    main()
