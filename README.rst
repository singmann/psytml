PsyTML
======

psytml.py contains a class for displaying a borderless html page (always on
top) with html forms. The html form needs to use method "get", then the
results are collected in object.data (i.e. a slot data of the object
created by the main class PsyTML).


*psytml.py* contains the following classes:

    * show_form(filename, size, position)
        shows a html form and returns the response as a Python dict

    * PsyTML(self, size, position)
        create an object for presenting html files
        o  *size* is the size of the html in pixel
        o  *position* is either a list of length two indicating the
            position (origin is top left) or True which corresponds to a
            central position.

    * PsyTML.viewPsyTml(self, html)
        display the specified html page
        o  *html* string with the location of an html file to be presented

The examples folder contains some simple examples.

**The examples/psychopy folder contains PsychoPy1.py a "complete"
experiment using PsychoPy and PyTML.**

Known Issus
-----------

* Does not run with psychopy full screen mode. If psychopy is run in
  full screen mode, the PsyTML window does not show up and the whole
  program "dead locks". (We are working on that :) )
* Some issues with non ascii characters in html text fields. Non ascii
  characters does not break the program, but you can sometimes only
  continue, when you remove all characters PsyTML does not like in the text
  field.

Henrik Singmann and Konstantin Sering, September 2012

