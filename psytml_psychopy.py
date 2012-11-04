#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# psytml_psychopy.py
#
# (c) 2012 Konstantin Sering <konstantin.sering [aet] gmail.com>
#
# GPL 3.0+ or (cc) by-sa (http://creativecommons.org/licenses/by-sa/3.0/)
#
# content:
#
# input: --
# output: --
#
# created 2012-11-04 KS
# last mod 2012-11-04 23:11 KS

"""
This module implements some psychopy specific behaviours and capsulates the
basic psytml module from psychopy.

"""

from PyQt4 import QtGui # needed for initializing Qt
from psychopy import misc

#should be a relative import
from psytml import PsyTML

def show_form(filename, size=(800, 600), position=None, fullscreen=False,
              units="pix", monitor=None, screen_resolution=None):
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
    fullscreen : *False* or True
        if True window state is set to WindowFullScreen.
    units : "pix", "deg", "cm" (optional)
        psychopy units to calculate size and position of the window. If units
        is different from "pix" monitor must be present. Default is "pix"
    monitor : psychopy.monitors.Monitor (optional)
        psychopy monitor object, that is used to convert units.
    screen_resolution : tuple (optional)
        screen_resolution (width, height) in pixel. Default to None. If None
        psytml guesses the screen resolution via

    """
    html_form = PsyTMLPsychopy(size, position, units, monitor,
                               screen_resolution)
    html_form.viewPsyTML(filename, fullscreen=fullscreen)
    return html_form.data


class PsyTMLPsychopy(PsyTML):
    """
    Add psychopy units support to PsyTML class.

    """

    def __init__(self, size=(800, 600), position=None, units="pix",
                 monitor=None, screen_resolution=None):
        """
        Parameters
        ----------

        size : *(800, 600)* or tuple
            tuple containing the width and the height of the window in pixel
        position : *None* or tuple
            if None QtWebKit default position is used, otherwise the position
            given in a tuple containing the left top pixel position of the
            window.
        units : "pix", "deg", "cm" (optional)
            psychopy units to calculate size and position of the window. If
            units is different from "pix" monitor must be present. Default is
            "pix."
        monitor : psychopy.monitors.Monitor (optional)
            psychopy monitor object, that is used to convert units.
        screen_resolution : tuple (optional)
            screen_resolution (width, height) in pixel. Default to None. If
            None psytml guesses the screen resolution via
            PyQt4.QtGui.QApplication.desktop().size()

        """
        if units != "pix":
            if not monitor:
                raise ValueError("if units is not 'pix', monitor must be supplied")

        # convert to pixel
        if units == "deg":
            size = [misc.deg2pix(x, monitor) for x in size]
            if position:
                position = [misc.deg2pix(x, monitor) for x in position]
        elif units == "cm":
            size = [misc.cm2pix(x, monitor) for x in size]
            if position:
                position = [misc.cm2pix(x, monitor) for x in position]

        # make pixel relative to center of the monitor
        if position:
            screen = screen_resolution
            if not screen_resolution:
                screen_size = QtGui.QApplication.desktop().size()
                screen = (screen_size.width(), screen_size.height())
            position = (position[0] + int(screen[0]/2.) - int(size[0]/2.),
                        position[1] + int(screen[1]/2.) - int(size[1]/2.))

        # call parent with calculated parameters
        super(PsyTMLPsychopy, self).__init__(size, position)

