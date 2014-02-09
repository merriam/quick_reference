Ledger-cli Quick Reference
==========================

Useful Links
============

* Main Sites:    [Main site](http://www.ledger-cli.org),  [Downloads](http://www.ledger-cli.org/download.html)
* Ledger-cli Development:  [Github Repository](https://github.com/ledger/ledger/), [Website Development](https://github.com/ledger/ledger-website), [Bugs](http://bugs.ledger-cli.org/describecomponents.cgi)
* Community:  [IRC (chat)](irc://irc.freenode.net/ledger),
* Documentation:  [Manual](http://www.ledger-cli.org/3.0/doc/ledger3.html) or as [PDF](http://www.ledger-cli.org/3.0/doc/ledger3.pdf), [Man page](http://www.ledger-cli.org/3.0/doc/ledger.1.html), [Wikipedia](https://en.wikipedia.org/wiki/Ledger_\(software\))
* Plug-ins:  [Vim](https://github.com/ledger/vim-ledger), [Emacs ledger-mode](http://www.ledger-cli.org/3.0/doc/ledger-mode.html), [Web Interface](https://github.com/ledger/ledger-web)
* Alternate Implementations:  [Haskell](https://github.com/ledger/ledger4) and [commodities](https://github.com/ledger/commodities), [Lisp](https://github.com/ledger/cl-ledger),
* People:  [John Wigley](https://github.com/jwiegley)

Command Line Options
-------------------------------------------------------------------------------

-f <input-file> | The input file
--strict | Require all accounts and metatags in transcations to have been declared with *account* and *?* lines.

Accounting Glossary
-------------------------------------------------------------------------------

Account|Anywhere where money can go.
Credit|An amount.  A positive number in Liability, Capital, and Income accounts.
Debit|An amount.  A positive number in Asset and Expense accounts.


Glossary
-------------------------------------------------------------------------------

Emacs Ledger-mode
----

See [Installation](http://www.ledger-cli.org/3.0/doc/ledger-mode.html#Quick-Installation).

* <Tab>     Auto-complete payees, account names
* C-c C-a   Prompt for date to add trascation in correct order
* C-c C-f <search item>   Narrow reports to search item.  Also, cancel previous Narrow command.
* C-c C-r C-o  Reports

* C-c C-c   Mark item as cleared


Quick Reports  (with C-c C-o C-r)
----

* account
* bal
* payee
* reg

Report window:
k = kill
e = edit report parameters
r = redo
<spc> = scroll
