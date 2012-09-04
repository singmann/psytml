import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *

elements = {"like":"", "text": ""}

class MyWebPage(QWebPage):
    def acceptNavigationRequest(self, frame, req, nav_type):
        if nav_type == QWebPage.NavigationTypeFormSubmitted:
            text = "<br/>\n".join(["%s: %s" % pair for pair in req.url().queryItems()])
            print(text)
            return True
        else:
            return super(MyWebPage, self).acceptNavigationRequest(frame, req, nav_type)


class Window(QWidget):
    def __init__(self, html):
        super(Window, self).__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)
        view = QWebView(self)
        layout = QVBoxLayout(self)
        layout.addWidget(view)
        view.setPage(MyWebPage())
        view.setHtml(html)
    

# setup the html form
html = """
<form action="" method="get">
Like it?
<input type="radio" name="like" value="yes"/> Yes
<input type="radio" name="like" value="no" /> No
<br/><input type="text" name="text" value="Hello" />
<input type="submit" name="submit" value="Send"/>
</form>
"""
        
def main():
    app = QApplication(sys.argv)
    
    window = Window(html)
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()
