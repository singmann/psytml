#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# psytml_psychopy.py
#
# (c) 2012 Konstantin Sering <konstantin.sering [aet] gmail.com>
# and Henrik Singmann
#
# GPL 3.0+ or (cc) by-sa (http://creativecommons.org/licenses/by-sa/3.0/)
#
# content:
#
# input: --
# output: --
#
# created 2012-11-04 KS
# last mod 2012-11-08 18:40 HS

"""
This module implements some psychopy specific behaviours and capsulates the
basic psytml module from psychopy.

"""

from PyQt4 import QtGui # needed for initializing Qt
from psychopy import misc

#should be a relative import
from psytml import PsyTML

def show_form(filename, size=(800, 600), position=None, fullscreen=False,
              units="pix", monitor=None):
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
        if None screen center, otherwise the position given in a tuple 
        containing the center of the window relative to the center of
        the screen (positive values mean up/right)
    fullscreen : *False* or True
        if True window state is set to WindowFullScreen.
    units : "pix", "deg", "cm", "norm" (optional)
        psychopy units to calculate size and position of the window. If units
        is different from "pix" monitor must be present. Default is "pix"
    monitor : psychopy.monitors.Monitor (optional)
        psychopy monitor object, that is used to convert units.


    """
    html_form = PsyTMLPsychopy(size, position, units, monitor)
    html_form.viewPsyTML(filename, fullscreen=fullscreen)
    return html_form.data


class PsyTMLPsychopy(PsyTML):
    """
    Add psychopy units support to PsyTML class.

    """

    def __init__(self, size=(800, 600), position=None, units="pix",
                 monitor=None):
        """
        Parameters
        ----------

        size : *(800, 600)* or tuple
            tuple containing the width and the height of the window in pixel
        position : *None* or tuple
            if None screen center, otherwise the position given in a tuple 
            containing the center of the window relative to the center of
            the screen (positive values mean up/right)
        units : "pix", "deg", "cm", "norm" (optional)
            psychopy units to calculate size and position of the window. If
            units is different from "pix" monitor must be present. Default is
            "pix."
        monitor : psychopy.monitors.Monitor (optional)
            psychopy monitor object, that is used to convert units.


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
        elif units == "norm":
            size = [int(monitor.getSizePix()[0] * (float(size[0])/2)), int(monitor.getSizePix()[1] * (float(size[1])/2))]
            if position:
                position = [int(monitor.getSizePix()[0] * position[0]), int(monitor.getSizePix()[1] * position[1])]
        else:
            raise ValueError("only 'pix', 'deg', 'cm', or 'norm' are accepted units.")
        
        # call parent with calculated parameters
        super(PsyTMLPsychopy, self).__init__(size, position)

