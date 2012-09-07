PsyTML
=====

PsyTML.py contains a class for displaying a borderless html page (always on top) 
with html forms. The html form needs to use method "get", then the results are
collected in object.data (i.e. a slot data of the object created by the main class
PsyTML).


*PsyTML.py* contains the following classes:

	* PsyTml(self, size, position = True)
		(create an object for presenting html files)
		o  *size* is the size of the html in pixel
		o  *position* is either a list of length two indicating the position (origin 
			is top left) or True which corresponds to a central position.
	
	* PsyTML has one method: viewPsyTml(self, html)
		(display the specified html page)
		o  *html* string with the location of an html file to be presented
	
	* Start(self, id, condition = False)
		(show a dialog with id and possibly condition. This class was written, 
		 because for the first time a PyQt Window is displayed above a pyglet window,
		 the background does not have the correct color. After running Start, it works)
		o  *id* Participant id
		o  *condition* Participant condition, the default (False) shows no condition.

The examples folder contains some simple examples.

**The examples/psychopy folder contains PsychoPy1.py a "complete" experiment using PsychoPy and PyTML.**

Henrik Singmann, September 2012
