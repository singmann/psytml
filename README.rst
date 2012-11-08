PsyTML
======

**psytml.py** contains the function ``show_form()`` for displaying a borderless 
html page (always on top) with html forms (using method "get"). 
Participants' responses are returned as a python dict.
(Actually ``show_form`` wraps class ``PsyTML``.)


- ``show_form(filename, size, position)``
        shows a html form and returns the response as a Python dict
        
        -  ``filename`` string, path to local html file containing the form.
        -  ``size`` tuple containing the width and the height of the window in 
           pixel.
        -  ``position`` either a tuple indicating the position (of the center 
           of the window, relative to the screen center) or None which 
           results in centering the window.

**psytml_psychopy.py** adds a ``norm`` argument to ``show_form`` adding `PsychoPy Units`_ ``"deg"``, ``"cm"``, ``"norm"`` for specifying window size and position (needs PsychoPy and a `PsychoPy Monitor Object`_). 

- ``show_form(filename, size=(800, 600), position=None, units="pix", monitor)``

The examples folder contains some examples, including a quasi complete experiment, see corresponding README.

Known Issues
------------

* Does not run with psychopy full screen mode. If psychopy is run in
  full screen mode, the PsyTML window does not show up and the whole
  program "dead locks". This, unfortunately is by design and cannot be 
  changed (see `Issue 10`_).
* Some issues with non ascii characters in html text fields. Non ascii
  characters does not break the program, but you can sometimes only
  continue, when you remove all characters PsyTML does not like in the text
  field.

Henrik Singmann and Konstantin Sering, November 2012

.. _PsychoPy Monitor Object: http://www.psychopy.org/general/monitors.html
.. _PsychoPy Units: http://www.psychopy.org/general/units.html
.. _Issue 10: https://github.com/singmann/psytml/issues/10

