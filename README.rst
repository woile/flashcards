========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis|
        | |codecov|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|

.. |docs| image:: https://readthedocs.org/projects/flashcards/badge/?style=flat
    :target: https://readthedocs.org/projects/flashcards
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/woile/flashcards.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/woile/flashcards

.. |codecov| image:: https://codecov.io/github/woile/flashcards/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/woile/flashcards

.. |version| image:: https://img.shields.io/pypi/v/flashcards.svg
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/flashcards

.. |commits-since| image:: https://img.shields.io/github/commits-since/woile/flashcards/v0.1.0.svg
    :alt: Commits since latest release
    :target: https://github.com/woile/flashcards/compare/v0.1.0...master

.. |wheel| image:: https://img.shields.io/pypi/wheel/flashcards.svg
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/flashcards

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/flashcards.svg
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/flashcards

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/flashcards.svg
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/flashcards


.. end-badges

small cli tool to study using fl

* Free software: BSD license

Installation
============

::

    pip install flashcards

Documentation
=============

https://flashcards.readthedocs.io/

Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
