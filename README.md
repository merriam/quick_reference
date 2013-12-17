quick_reference
===============

Quick Reference generator, like the RGruet Python Guide.  Currently for Docker Quick Reference.

This code generates quick reference guides.

FileList
--------

* quick.py -- The HTML generator functions
* quick_docker.py -- Specific code for the Docker Quick Reference Guide
* quick_flask.py -- Unfinished Flask framework quick reference
* css/ -- A directory of CSS pages copied from RGruet's guide
* make -- A shell script to build flask/ and docker/ output directories
* docker/quick_docker.html -- Docker Quick Reference page
* flask/quick_flask.html -- Flask Quick Reference page

Run 'python3 quick_docker.py' to get HTML output to the terminal.

Dependencies
------------

Python3
Markdown (https://pypi.python.org/pypi/Markdown)
