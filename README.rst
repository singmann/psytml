PsyTML
======

psytml.py contains a class for displaying a borderless html page (always on
top) with html forms. The html form needs to use method "get", then the
results are collected in object.data (i.e. a slot data of the object
created by the main class PsyTML).


*psytml.py* contains the following classes:

- show_form(filename, size, position)
        shows a html form and returns the response as a Python dict

- PsyTml(self, size=(800, 600), position=None)
        (create an object for presenting html files)

        -  *size* is the size of the html in pixel
        -  *position* is either a list of length two indicating the
           position (origin is top left) or None which results in centering
           the window.

- PsyTML has one method: viewPsyTml(self, html)
        (display the specified html page)

        -  *html* string with the location of an html file to be presented

The examples folder contains some simple examples.

**The examples/psychopy folder contains PsychoPy1.py a "complete"
experiment using PsychoPy and PyTML.**

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

Henrik Singmann and Konstantin Sering, October 2012

.. _Issue 10: https://github.com/singmann/psytml/issues/10

