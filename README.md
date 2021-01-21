# pyMenus

### Introduction
pyMenus is a collection of classes that create CLI menus and prints them to the terminal.
Return either the index of the user's response or the object that the user chooses.
Useful for quickly creating simple CLI user interfaces.

### Technologies
Written in pure Python, no other dependencies. Created with **Python 3.9**. Untested with earlier versions.

### Installation
git clone git@github.com:IXIXIXIXIXIXIXIXIX/pyMenus.git

### Use
Constructor for both IntReturnMenu and ObjectReturnMenu take a list of objects as an argument and a 
string as an optional argument. The optional arg is the string that prompts the user to choose an 
option. Absent this argument, there is a default.

Ensure that the objects in your list are either human-readable strings or have their \_\_str\_\_ 
defined as recognisable unique strings as this is what the user will be presented to choose from.

Instances of IntReturnMenu will return the index of the object that the user selects as an *int*.
Instances of ObjectReturnMenu will return the object chosen by the user.

IntReturnMenu lends itself particularly well to lists of strings, with the return indicating which 
of several different programmatic pathways to progress.
