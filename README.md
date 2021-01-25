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
Constructor for both **IntReturnMenu** and **ObjectReturnMenu** take a list of objects as an argument and a 
string as an optional argument. The optional arg is the string that prompts the user to choose an 
option. Absent this argument, there is a default.

Ensure that the objects in your list are either human-readable strings or have their \_\_str\_\_ 
defined as recognisable unique strings as this is what the user will be presented to choose from.

For both classes included, once instantiated, the menu will be printed and user response returned 
by invoking the `choose()` method. The `choose()` method takes an optional boolean argument (defaults
to `False`), confirm. If `True` is passed into the method (e.g. `class_instance.choose(True)`), the
user will be prompted to confirm their choice after making their initial selection.

When the `choose()` method is called, instances of **IntReturnMenu** will return the index of the object 
that the user selects as an *int*.

When the `choose()` method is called, instances of **ObjectReturnMenu** will return the object instance 
chosen by the user.

**IntReturnMenu** lends itself particularly well to lists of strings, with the return indicating which 
of several different programmatic pathways to progress.

Also included is the standalone funtion **binary_choice**. This takes an optional string argument.
When invoked, `binary_choice(query)` prompts the user for a Y or N response at the terminal. The prompt is 
comprised of the optional string argument (default: "*Confirm*") concatenated with "*(Y/N)? *".

All methods and functions loop until a permitted response is received from the user. Alpha user responses  
are not case sensitive.
