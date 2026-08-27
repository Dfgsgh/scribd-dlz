# scribd-dlz


 **Download documents from Scribd in pdf format**

 Scribd-dlz uses selenium and headless Chrome to take high resolutions screenshots of the document pages, and eventually merges them into a pdf file.

Scribd-dlz is an updated fork of scribd-dl, which can be found here:
`https://github.com/g-nie/scribd-dl`

## Usage



    $ scribd-dlz url [-p PAGES] [-v]

Examples :

    $ scribd-dlz https://www.scribd.com/document/90403141/Social-Media-Strategy
    $ scribd-dlz scribd.com/document/351688288 scribd.com/document/90403141 -p 1-3
    $ scribd-dlz https://www.scribd.com/document/352366744 --pages 10-16
    $ scribd-dlz scribd.com/document/351688288 -p 20 --verbose


Scribd-dlz can also be used directly in a python script, however such use is not documented (yet).

## Installation

### Step 1: clone the repository
Do it via the commandline like this:

`$ git clone https://github.com/Dfgsgh/scribd-dlz.git`

You can also use an other method.

### Step 2: open a commandline in the directory the repository has been cloned to

The easiest way is just to cd there, like this:
`$ cd scribd-dlz`

### Step 3: install using pip
`$ pip install .`

Chromedriver is required in order to work. See all available chromedriver downloads here:
`https://sites.google.com/a/chromium.org/chromedriver/downloads`

Put the chromedriver executable in your system PATH variable.
Scribd-dlz supports **Python 3.11.4+** and possibly older versions



