""" quick.py -- quick reference generator common routines.

There are styles and levels of code.   This is currently written as the 'dirty hack' without
unittests, system tests, documentation, or really anything other than the need to get the job
done.

The clients are expected to initimate with this code.

"""

from markdown import markdown

def mark(s):
    marked = markdown(s)
    if marked[:3] == "<p>" and marked[-4:] == "</p>":
        marked = marked[3:-4]
    return marked

def dec_html_trace(func):
    def trace_copy(*args, **kwargs):
        """ decorator to trace calls to html functions """
        if args and kwargs:
            arglist = (", ".join((repr(arg) for arg in args)) +
                       ", " +
                       ", ".join((str(key)+"="+repr(value) for key, value in kwargs.items())))
        elif args:
            arglist = ", ".join((repr(arg) for arg in args))
        elif kwargs:
            arglist = ", ".join((str(key)+"="+repr(value) for key, value in kwargs.items()))
        else:
            arglist = ""
        as_called_long = "{}({})".format(func.__name__, arglist)
        as_called_short = "{}(...)".format(func.__name__)
        as_called = as_called_long if len(as_called_long) < 30 else as_called_short
        ret_html = func(*args, **kwargs)
        return "<!-- begin {0} -->\n{1}\n<!-- end {0} -->\n".format(as_called, ret_html)
    return trace_copy

def anchor_name(name):
    name = name.replace(" ", "")   # id fields may not have spaces.
    return name

def anchor(name):
    """ return in document anchor, for links to '#name' """
    return '<a name="{0}" id ="{0}"></a>\n'.format(anchor_name(name))

def section_title(name):
    return "<h2>\n{}{}\n</h2>\n".format(anchor(name), name)

g_toc_list = []
def toc_add(name, subheading=False, toc_list=g_toc_list): # pylint: disable=dangerous-default-value
    """ records to toc_list, no return value. """
    if subheading:
        toc_list.append(">"+name)
    else:
        toc_list.append(name)


def toc():
    p = [ section_title("Contents"), "<ul>" ]
    items = g_toc_list[:]   # copy because pop loop is destructive
    while items:
        item = items.pop(0)
        p.append('<li><a href="#{}">{}</a>'.format(anchor_name(item), item))
        subs = []
        while items and items[0][0] == ">":  # while subheadings are next.
            subs.append(items.pop(0)[1:])  # drop ">"
        if subs:
            p.append(": ")
            sub_items = ['<a href="#{}">{}</a>'.format(anchor_name(sub), sub) for sub in subs]
            p.append(", ".join(sub_items))
    p.append("</ul>")
    return "\n".join(p)

def head(title):
    p = [ '<!DOCTYPE html>\n<html>\n\n<head>\n<title>{}</title>\n'.format(title) ]
    p.append("""
    <link href="css/modern.css" rel="stylesheet" type="text/css" title="Modern" media="all" />
    <link href="css/modernbw.css" rel="alternate stylesheet" type="text/css" title="Modern Black &amp; White" media="all" />
    <link href="css/modern-colored.css" rel="stylesheet" type="text/css" title="Modern Colored" media="all" />
    <link href="css/classic.css" rel="alternate stylesheet" type="text/css" title="Classic" media="all" />
    <link href="css/highcontrast.css" rel="alternate stylesheet" type="text/css" title="High contrast" media="all" />
    <link href="css/printing.css" rel="alternate stylesheet" type="text/css" title="Printing" media="all" />
    <script type="text/javascript" src="css/styleswitcher.js"></script>
""")
    p.append("<body>\n")
    p.append(anchor('top'))
    p.append("""
    <table class="main" summary="Layout" border="0" cellpadding="0">
    <tbody>
    <tr>
      <td colspan="20" class="logo" height="59">
      <h1> {} </h1>
      </td>
    </tr>
    <tr>
      <td class="content">
      """.format(title))
    p.append('<style type="text/css">\n'
             'div.subheader {background-color:#B4B4FA;font-style:italic;}\n'
             '</style>')
    p.append("""
        <p><span class="noprint"> Style chooser:
          <a href="#" onclick="setActiveStyleSheet('Modern'); return false;" title="Modern style (default)">Modern</a>,
          <a href="#" onclick="setActiveStyleSheet('Modern Black &amp; White'); return false;" title="Modern B&amp;W style, good for printing">Modern B&amp;W</a>,
          <a href="#" onclick="setActiveStyleSheet('Modern Colored'); return false;" title="Modern variant, slightly Colored">Modern Colored</a>,
          <a href="#" onclick="setActiveStyleSheet('Classic'); return false;" title="Classic (original) layout">Classic</a>,
          <a href="#" onclick="setActiveStyleSheet('High contrast'); return false;" title="Black &amp; White">High contrast</a>
          or <a href="#" onclick="setActiveStyleSheet('Printing'); return false;" title="Optimized for A4 paper">Printing</a>
        </span><br />
        <span  class="noprint" style="font-size:x-small"><span style="color:red">[Hint</span>: Use styles Modern B&amp;W or
          Printing to print. If you get problems, try printing the <a href="http://charlesmerriam.com/#QuickRef" title="PDF versions">
          PDF versions</a> instead]</span>
        </p>
        """)
    # TODO:  Fix the link to where pdfs exist.
    return "\n".join(p)

def tail():
    return "</table>\n"

def link(url, title=None):
    """ return an href to a url in a new window """
    if not title:
        title = url
    return '<a target="_blank" href="{0}">{1}</a>'.format(url, title)

def links_line(name, url_name_pairs):
    """ line of title and links """
    links = ", \n".join([link(url, title) for url, title in url_name_pairs])
    return "<b>{}</b>:\n{}".format(name, links)

def link_section(section_name, lines):
    toc_add(section_name)
    title = section_title(section_name)
    start = '<blockquote class="link_section">\n<ul>'
    middle = ''.join(["<li>\n{}</li>\n".format(line) for line in lines])
    end  = '</ul>\n</blockquote>'
    return '\n'.join((title, start, middle, end))

def table1(name=None, caption=None, widths=None, headers=None, cell_lines=None):
    cells_per_line = len(headers) if headers else 0
    p = []
    if name:
        toc_add(name)
        p.append(section_title(name))
    p.append("<table>")
    if caption:
        p.append("<caption>{}</caption>".format(caption))
    if headers:
        p.append("<thead><tr>")
        for i in range(len(headers)):
            if widths:
                assert len(widths) == len(headers)
                p.append('<th width="{}">{}'.format(widths[i], headers[i]))
            else:
                p.append('<th>{}'.format(headers[i]))
    p.append("<tbody>")
    for cells in cell_lines:
        p.append("<tr>")
        for cell in cells:
            p.append("<td>{}".format(mark(cell)))
        for _ in range(cells_per_line - len(cells)):
            p.append("<td> ")
    p.append("</table>")
    return "\n".join(p)


def table(table_name, caption, headers, cell_lines):
    p = []
    if table_name:
        p.append(table_name)
    p.append("<table>")
    if caption:
        p.append("<caption>{}</caption>".format(caption))
    if headers:
        p.append("<thead><tr>")
        for heading in headers:
            p.append('<th>{}'.format(heading))
    p.append("<tbody>")
    for body in cell_lines:
        p.append("<tr>")
        for cell in body:
            p.append("<td>{}".format(mark(cell)))
    p.append("</table>")
    return "\n".join(p)

