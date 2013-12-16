""" Flask specific routines.   Not yet working. """

# Copyright (c) 2013 Charles Merriam

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from markdown import markdown
from quick import *


def flask_useful_links():
    """ put out the flask quick reference guide """
    flask = links_line("Flask web development micro-framework", [
        ("http://flask.pocoo.org", "Overview"),
        ("https://flask.readthedocs.org/en/latest/", "Documentation"),
        ("https://flask.readthedocs.org/en/latest/installation/#installation", "Installation"),
        ("https://pypi.python.org/pypi/Flask", "PyPI"),
        ("https://flask.readthedocs.org/en/latest/tutorial/#tutorial", "Tutorial"),
        ("https://github.com/mitsuhiko/flask", "GitHub repository"),
        ("https://github.com/mitsuhiko/flask/issues", "Bugs and issues"),
        ("http://stackoverflow.com/questions/tagged/flask", "Stack Overflow"),
        ("https://flask.readthedocs.org/en/latest/license/#flask-license", "License")
        ])

    jinja = links_line("Jinja2 friendly templating language", [
        ("http://jinja.pocoo.org", "Overview"),
        ("https://jinja2.readthedocs.org/en/latest/", "Documentation"),
        ("https://pypi.python.org/pypi/Jinja2", "PyPI"),
        ("https://github.com/mitsuhiko/jinja2", "GitHub repository"),
        ("https://github.com/mitsuhiko/jinja2/issues", "Bugs and issues"),
        ("http://stackoverflow.com/questions/tagged/jinja2", "Stack Overflow"),
        ("https://github.com/mitsuhiko/jinja2/blob/master/LICENSE", "License")
        ])

    werk = links_line("Werkzeug Python WSGI Utility Library", [
        ("http://werkzeug.pocoo.org", "Overview"),
        ("https://werkzeug.readthedocs.org/en/latest/", "Documentation"),
        ("https://werkzeug.readthedocs.org/en/latest/installation/", "Installation"),
        ("https://pypi.python.org/pypi/Werkzeug", "PyPI"),
        ("https://github.com/mitsuhiko/Werkzeug", "GitHub repository"),
        ("https://github.com/mitsuhiko/Werkzeug/issues", "Bugs and issues"),
        ("http://stackoverflow.com/questions/tagged/werkzeug", "Stack Overflow"),
        ("https://github.com/mitsuhiko/werkzeug/blob/master/LICENSE", "License")
        ])

    other = links_line("Other Links and tools", [
        ("http://docs.python.org/3.3/library/sqlite3.html", "SQLLite")
        ])
       # IRC channel?  More mailing lists?
    return link_section("Useful Links", (flask, jinja, werk, other))

def flask_main():
    """ put out the flask quick reference guide """

    print( head("Flask, Jinja2, and Werkzeug Quick Reference"),
           flask_useful_links()
         )


def vagrant_commands():
    # box = "list (list available boxes)| repackage <name> <provider> | -f (--force) force overwrite | --insecure No SSL | --provider ??? "
    # common = "vagrant up, vagrant ssh"
    # vagrant file comments
    return ""

if __name__ == "__main__":
    flask_main()
