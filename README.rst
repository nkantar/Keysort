Keysort: Sorting Lists of Dictionaries
========================================================

**Keysort** is small utility for sorting lists of dictionaries by dictionary keys and lists of objects by attributes.


Examples
--------

Sorting dictionaries by keys:

.. code-block:: python

    >>> from keysort import keysort
    >>>
    >>> my_list = [{'code': 'beta',    'number': 3},
                   {'code': 'delta',   'number': 2},
                   {'code': 'alpha',   'number': 0},
                   {'code': 'beta',    'number': 2},
                   {'code': 'charlie', 'number': 1}]
    >>>
    >>> keysort(my_list, ['code', 'number'])
    [{'code': 'alpha',   'number': 0},
     {'code': 'beta',    'number': 2},
     {'code': 'beta',    'number': 3},
     {'code': 'charlie', 'number': 1},
     {'code': 'delta',   'number': 2}]
    >>>
    >>> keysort(my_list, ['number', 'code'])
    [{'code': 'alpha',   'number': 0},
     {'code': 'charlie', 'number': 1},
     {'code': 'beta',    'number': 2},
     {'code': 'delta',   'number': 2},
     {'code': 'beta',    'number': 3}]

Sorting objects by attributes:

.. code-block:: python

    >>> from dataclasses import dataclass
    >>> from keysort import attrsort
    >>>
    >>> @dataclass
    ... class MyObj:
    ...     code: str
    ...     number: int
    ...
    >>> my_list = [MyObj(code='beta',    number=3),
    ...            MyObj(code='delta',   number=2),
    ...            MyObj(code='alpha',   number=0),
    ...            MyObj(code='beta',    number=2),
    ...            MyObj(code='charlie', number=1)]
    >>>
    >>> attrsort(my_list, ['code', 'number'])
    [MyObj(code='alpha',   number=0),
     MyObj(code='beta',    number=2),
     MyObj(code='beta',    number=3),
     MyObj(code='charlie', number=1),
     MyObj(code='delta',   number=2)]
    >>>
    >>> attrsort(my_list, ['number', 'code'])
    [MyObj(code='alpha',   number=0),
     MyObj(code='charlie', number=1),
     MyObj(code='beta',    number=2),
     MyObj(code='delta',   number=2),
     MyObj(code='beta',    number=3)]


Install
-------

.. code-block:: shell

    pip install keysort


Contributing
------------

Contributions of all sorts are welcome, be they bug reports, patches, or even just feedback. Creating a `new issue <https://github.com/nkantar/Keysort/issues/new>`_ or `pull request <https://github.com/nkantar/Keysort/compare>`_ is probably the best way to get started.

Please note that this project is released with a `Contributor Code of Conduct <https://github.com/nkantar/Keysort/blob/master/CODE_OF_CONDUCT.md>`_. By participating in this project you agree to abide by its terms.
