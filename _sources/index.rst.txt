.. mzgpaul-test-pkg documentation master file, created by
   sphinx-quickstart on Wed Dec 25 20:14:42 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

mzgpaul-test-pkg documentation
==============================

.. include:: ../../README.md
    :parser: myst_parser.sphinx_

blabla

Quick setup
-----------
install it using pip:

.. code-block:: console

   (.venv) $ pip install YOUR_PKG

This is a cross-reference to document :doc:`installation`.
This is another cross :ref:`my-labeltext <my-label>`


Contents
--------
.. toctree::
    :maxdepth: 2
    :caption: YOUR CAPTION

    installation
    modules


This is a reference to function :py:func:`mzgpaul_test_pkg.arithmetics.add`
