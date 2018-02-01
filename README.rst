Keysort: Sorting Lists of Dictionaries
========================================================

**Keysort** is small utility for sorting lists of dictionaries by dictionary key.

.. image:: https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg 
   :target: https://saythanks.io/to/nkantar


Examples
--------

.. code-block:: python

    >>> from keysort import keysort
    >>> my_list = [{'code': 'beta',    'number': 3},
                   {'code': 'delta',   'number': 2},
                   {'code': 'alpha',   'number': 0},
                   {'code': 'beta',    'number': 2},
                   {'code': 'charlie', 'number': 1}]
    >>> keysort(my_list, ['code', 'number'])
    [{'code': 'alpha',   'number': 0},
     {'code': 'beta',    'number': 2},
     {'code': 'beta',    'number': 3},
     {'code': 'charlie', 'number': 1},
     {'code': 'delta',   'number': 2}]
    >>> keysort(my_list, ['number', 'code'])
    [{'code': 'alpha',   'number': 0},
     {'code': 'charlie', 'number': 1},
     {'code': 'beta',    'number': 2},
     {'code': 'delta',   'number': 2},
     {'code': 'beta',    'number': 3}]


Install
-------

.. code-block:: shell

    pip install keysort


Contributing
------------

Contributions of all sorts are welcome, be they bug reports, patches, or even just feedback. Creating a `new issue <https://github.com/nkantar/Keysort/issues/new>`_ or `pull request <https://github.com/nkantar/Keysort/compare>`_ is probably the best way to get started.

Please note that this project is released with a `Contributor Code of Conduct <https://github.com/nkantar/Keysort/blob/master/CODE_OF_CONDUCT.md>`_. By participating in this project you agree to abide by its terms.
