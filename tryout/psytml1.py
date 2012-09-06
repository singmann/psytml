import sys
from urllib import unquote_plus

from PyQt4 import QtCore, QtGui, QtWebKit

class MyWebPage(QtWebKit.QWebPage):
    formSubmitted = QtCore.pyqtSignal(QtCore.QUrl)

    def acceptNavigationRequest(self, frame, req, nav_type):
        if nav_type == QtWebKit.QWebPage.NavigationTypeFormSubmitted:
            self.formSubmitted.emit(req.url())
        return super(MyWebPage, self).acceptNavigationRequest(frame, req, nav_type)

class Window(QtGui.QWidget):
    def __init__(self, html, elements):
        super(Window, self).__init__()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        view = QtWebKit.QWebView(self)
        layout = QtGui.QVBoxLayout(self)
        layout.addWidget(view)
        layout.setContentsMargins(0, 0, 0, 0)
        view.setPage(MyWebPage())
        view.setHtml(html)
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
        for item in elements.iteritems():
            print '"%s" = "%s"' % item
        QtGui.qApp.quit()

# setup the html form
html = """
<form action="" method="get">
Like it?
<input type="radio" name="like" value="yes"/> Yes
<input type="radio" name="like" value="no" /> No
<br/><input type="text" name="text" value="" />
<input type="submit" name="submit" value="Send"/>
</form>
"""

def main():
    f1 = {}
    app = QtGui.QApplication(sys.argv)
    window = Window(html, f1)
    window.show()
    app.exec_()
    print(f1)

if __name__ == "__main__":
    main()
