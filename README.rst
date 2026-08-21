
=========
scribd-dlz
=========



|
| **Download documents from Scribd in pdf format**
|
| Scribd-dlz uses selenium and headless Chrome to take high resolutions screenshots of the document pages, and eventually merges them into a pdf file.

Usage
------------

.. code-block:: shell

    $ scribd-dlz (https://www.)scribd.com/(doc|document|presentation)/(document_id)/* [-p PAGES] [-v]

Examples ::

    $ scribd-dlz https://www.scribd.com/document/90403141/Social-Media-Strategy
    $ scribd-dlz scribd.com/document/351688288 scribd.com/document/90403141 -p 1-3
    $ scribd-dlz https://www.scribd.com/document/352366744 --pages 10-16
    $ scribd-dlz scribd.com/document/351688288 -p 20 --verbose

you can embed scribd-dlz, using a context manager like this:

.. code-block:: python

    import scribd_dlz

    options = {
        'pages': '1-3',
        'log-level': '2'  # info
    }
    with scribd_dlz.ScribdDLZ(options) as session:
        session.download([
            'https://www.scribd.com/document/352366744/',
            'https://www.scribd.com/document/351688288/'
        ])

use different page ranges in each document:

.. code-block:: python

    import scribd_dlz

    with scribd_dlz.ScribdDLZ() as session:
        session.download('https://www.scribd.com/document/352366744/', pages='1-3')
        session.download('https://www.scribd.com/document/351688288/', pages='3-5')
        for title in session.doc_titles:
            print(title)


Installation
------------
Clone it ::

    $ git clone https://github.com/Dfgsgh/scribd-dlz.git
    $ cd scribd-dl
    $ pip install .

-------------
| Chromedriver is required in order to work. See all available chromedriver downloads `here`_.
| Put the chromedriver executable in the assets folder or in your system PATH variable.
| Tested to work with chromedriver v2.37 and Chrome v65.0.
| Scribd-dlz supports **Python 3.11.4+** and possibly older versions

.. _`here`: https://sites.google.com/a/chromium.org/chromedriver/downloads
