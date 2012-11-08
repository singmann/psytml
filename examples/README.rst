PsyTML Examples
===============

This folder contains examples for PsyTML.

Files
-----

- ``psytml_example_single.py`` A single html page containing form elements.
- ``psytml_example_multiple.py`` Several html pages containing form elements.
- ``psytml_psychopy_example.py`` The same html form element using the different PsychoPy units.

Folders
-------

- **psychopy** A "full" experiment with instruction screens followed by several items in random order and a demographic questionnaire. Experiment has several between-subjects conditions, which is determined by the ``id.lst`` file. Data from items is written to a single file per participant (one row per trial), demographic data to a file with all participants (one row per participant). 
  *Monitor information (e.g., name and size) should be changed prior to running the file.*
- **fullscreen** A "full" experiment similar to the **psychopy** example, but screen size should be detected automatically, so it should always run in fullscreen.
- **sampleHTML** contains the HTML pages for the examples. Furthermore the JavaScript code for checking if a response is given.


Henrik Singmann and Konstantin Sering, November 2012

