# version 1.0: 7th September 2012
# Henrik Singmann with help from ekhumoror (http://stackoverflow.com/users/984421/ekhumoro)
# License: GPL v3

from urllib import unquote_plus
from PyQt4 import QtCore, QtGui, QtWebKit
import os

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
    def __init__(self, size, position = True):
        super(PsyTML, self).__init__()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.resize(size[0], size[1])
        self.position = position
        if (self.position != True):
            self.move(self.position[0], self.position[1])
        self.data = {}
        self.view = QtWebKit.QWebView(self)
        layout = QtGui.QVBoxLayout(self)
        layout.addWidget(self.view)
        layout.setContentsMargins(0, 0, 0, 0)
        self.view.setPage(MyWebPage())
        self.view.page().formSubmitted.connect(self.handleFormSubmitted)

    def viewPsyTML(self, html):
        if os.path.isfile(html):
            page = "file:///" + os.path.abspath(html).replace("\\", "/")
            self.view.setUrl(QtCore.QUrl(page))
        else:
            print('Error, following html file not found:' + html)
            return True
        if (self.position == True):
            self.center()
        self.exec_()
    
    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def handleFormSubmitted(self, elements):
        self.data = elements
        self.accept()



class Start(QtGui.QDialog):
    def __init__(self, id, condition = False):
        super(Start, self).__init__()
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.id = id
        self.condition = condition
        font = QtGui.QFont()
        font.setPointSize (14)
        self.setFont(font)
        self.initUI()
    
    
    def initUI(self):               
        id_lab = QtGui.QLabel('Id (#): ')
        id_edit = QtGui.QLineEdit()
        id_edit.setMaxLength(5)
        id_edit.setText(str(self.id))
        id_edit.setReadOnly(True)
        okButton = QtGui.QPushButton("OK")
        okButton.clicked.connect(self.close)       
        #cancelButton = QtGui.QPushButton("Cancel!")
        #cancelButton.clicked.connect(QtCore.QCoreApplication.instance().quit)       
        
        hbox = QtGui.QHBoxLayout()
        hbox.addWidget(id_lab)
        hbox.addWidget(id_edit)
        vBox = QtGui.QVBoxLayout()
        vBox.addLayout(hbox)
        
        if (self.condition != False):
            hboxC = QtGui.QHBoxLayout()
            condition_lab = QtGui.QLabel('Condition: ')
            condition_edit = QtGui.QLineEdit()
            condition_edit.setText(str(self.condition))
            condition_edit.setReadOnly(True)
            hboxC.addWidget(condition_lab)
            hboxC.addWidget(condition_edit)
            vBox.addLayout(hboxC)
        
        hbox2 = QtGui.QHBoxLayout()
        hbox2.addStretch(1)
        #hbox2.addWidget(cancelButton)
        hbox2.addWidget(okButton)
        
        vBox.addLayout(hbox2)
        self.setLayout(vBox)
        
        self.setWindowTitle('Starting Experiment')    
        self.center()
        self.exec_()
        
    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

