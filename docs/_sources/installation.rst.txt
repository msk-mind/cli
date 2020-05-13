Installation
============

Build from Source Code
----------------------

1. Git clone project

.. code-block:: bash

    git clone https://github.com/msk-mind/cli.git

2. Set up environment for CLI

.. code-block:: bash

    # create a virtual environment
    python -m venv env # or python3
    source env/bin/activate

    # install required libraries in the env
    pip install -r requirements.txt

3. (Optional) Generate executable

.. code-block:: bash

    pyinstaller --onefile mind.py

The executable will be at ``dist/mind``.

4. Test executable.

.. code-block:: bash

    $ ./dist/mind

    Usage: mind [OPTIONS] COMMAND [ARGS]...

      Welcome to MSK MIND!

    Options:
      --host TEXT  [default: http://localhost:8080]
      --help       Show this message and exit.

    Commands:
      download        download data.
      list-columns    show available columns given database and table.
      list-databases  show available databases.
      list-tables     show available tables given a database.
      query           query data.


Download
--------
TODO - provide macOS, linux executables in bin/ upon release.
