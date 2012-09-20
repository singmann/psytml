#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2012 Henrik Singmann with help from ekhumoror
# (http://stackoverflow.com/users/984421/ekhumoro)
# and Konstantin Sering <konstantin.sering [at] gmail.com>
# License: GPL v3
# last mod 2012-09-20 21:09 KS

"""
psytml provides a convenient way to present a html form at the screen and get
the form's data into python.

"""

from urllib import unquote_plus
from PyQt4 import QtCore, QtGui, QtWebKit
import os


def show_form(filename, size=(800, 600), position=None):
    """
    shows the form and returns the get variables as a Python dict.

    show_form has the same features and limitations as the PsyTML class.

    Parameters
    ----------

    filename : string
        path to html file containing the form.
    size : *(800, 600)* or tuple
        tuple containing the width and the height of the window in pixel.
    position : *None* or tuple
        if None QtWebKit default position is used, otherwise the position
        given in a tuple containing the left top pixel position of the
        window.

    """
    html_form = PsyTML(size, position)
    html_form.viewPsyTML(filename)
    return html_form.data

class MyWebPage(QtWebKit.QWebPage):
    """
    a small webpage handling the navigation bar ??.

    Why do we need this class?

    """
    formSubmitted = QtCore.pyqtSignal(object)

    def acceptNavigationRequest(self, frame, req, nav_type):
        if nav_type == QtWebKit.QWebPage.NavigationTypeFormSubmitted:
            elements = {}
            for key, value in req.url().encodedQueryItems():
                key = unquote_plus(bytes(key)).decode('utf8')
                value = unquote_plus(bytes(value)).decode('utf8')
                elements[key] = value
            self.formSubmitted.emit(elements)
        return super(MyWebPage, self).acceptNavigationRequest(frame, req,
                nav_type)

class PsyTML(QtGui.QDialog):
    """
    convenient object to show html files and collect the data out of a
    submitted form.

    Features
    --------

    * present html forms with JavaScript and css
    * data that is submitted is collected in a Python dict
    * multiple pages are possible

    Limitations
    -----------

    * only local html files are supported at the moment
    * only GET method is supported to transmit data to Python

    Known Bugs
    ----------

    * sometimes runs into troubles, when non ascii letters are used in a text
      field

    """
    def __init__(self, size=(800, 600), position=None):
        """
        Parameters
        ----------

        size : *(800, 600)* or tuple
            tuple containing the width and the height of the window in pixel
        position : *None* or tuple
            if None QtWebKit default position is used, otherwise the position
            given in a tuple containing the left top pixel position of the
            window.

        """
        super(PsyTML, self).__init__()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint |
                QtCore.Qt.WindowStaysOnTopHint)
        self.resize(size[0], size[1])

        self.position = position
        if not position is None:
            self.move(self.position[0], self.position[1])
        self.data = {}
        self.view = QtWebKit.QWebView(self)
        layout = QtGui.QVBoxLayout(self)
        layout.addWidget(self.view)
        layout.setContentsMargins(0, 0, 0, 0)
        self.view.setPage(MyWebPage())
        self.view.page().formSubmitted.connect(self.handleFormSubmitted)

    def viewPsyTML(self, html):
        """
        load a html file and present it on the screen.

        """
        if os.path.isfile(html):
            page = "file:///" + os.path.abspath(html).replace("\\", "/")
            self.view.setUrl(QtCore.QUrl(page))
        else:
            # TODO raise an exception here? (Zen of Python: Errors should never
            # pass silently. Unless explicitly silenced.)
            print('Error, following html file not found:' + html)
            return True
        if self.position is None:
            self.center()
        self.exec_()

    def center(self):
        """
        center the window on the screen.

        """
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def handleFormSubmitted(self, elements):
        """
        store the received data in self.data.

        """
        self.data = elements
        self.accept()

