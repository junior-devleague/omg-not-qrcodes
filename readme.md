---
author:
- gitten
title: 'OMG, Q Argh codes!'
type: Activity
---

Summary
=======

Activity for processing Python Dictionaries and building 2D arrays.
Thinking of programming as 'transformation of data' is a useful
perspective that can aid in reasoning about your program. Also,
Visualizing data is a very useful tool and can aid in debugging.

Objective (wip)
===============

ARG, matey. Your task is to put together the QR code described by a
Python Dictionary! Use the dictionary keys to transform the data into a
2D array structure of ones and zeroes. Then test that your array is
correctly formed by testing the QR code! ... arrrgh

Prerequisites
=============

-   Basic usage of Python REPL
-   Basic understanding of processing/building Python Lists (strings are
    lists too!)

Requirements (wip)
==================

-   shell terminal or Python IDE
-   Tkinter module, the standard python interface for the TK GUI toolkit
-   import the provided QR code activity library `q_arrgh`
-   Do you like puzzlely challenges? Yes, you do!

Desired Outcomes
================

-   Build an intuition about data represented as nested lists and
    dictionaries
-   Build an intuition about 'data transformation'
-   Basic understanding of processing dictionaries
-   Basic understanding of structuring 2D arrays (nested lists)
-   Increase confort level of utilizing the REPL for development
-   Preparation for Conway's Game of Life project

Tasks (wip)
===========

Preparing the activity
----------------------

### From the terminal

1.  Ensure Tkinter is installed

    ``` {.bash}
    sudo apt install python3-tk
    ```

2.  Clone the activity repository, change to project directory

    ``` {.bash}
    git clone https://github.com/junior-devleague/omg-not-qrcodes.git
    cd omg-not-qrcodes
    ```

3.  Create a virtual enviornment and install dependencies

    ``` {.bash}
    virtualenv -p python3 env/
    env/bin/pip install matplotlib
    ```

4.  start your REPL and import activity lib
    -   From terminal, enter `env/bin/python`
    -   In your newly started REPL, enter `import q_arrgh`

Q ARRGh\~\~
-----------

### Exploring the dictionary (wip)

### Visualize the data! (wip)

Additional Resources
====================

Genral functions that might be useful
-------------------------------------

-   `str(an_Integer)`
-   `int(a_String_that_represents_an_Integer)`

Expressions and functions for dictionaries that might be useful
---------------------------------------------------------------

-   `iter.keys()`
    -   Example:

        ``` {.python}
        dict = {"str": 808, 1234: False}
        for key in iter.keys(dict):
            print(dict[key])
        ```

-   `iter.items()`
    -   Example:

        ``` {.python}
        dict = {"str": 808, 1234: False}
        for key, value in iter.items(dict):
            print(key, value)
        ```
