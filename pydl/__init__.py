# Licensed under a 3-clause BSD style license - see LICENSE.rst
# -*- coding: utf-8 -*-
"""
====
pydl
====

Python replacements for functions that are part of the IDL_ built-in library, or
part of astronomical IDL libraries.  The emphasis is on reproducing results of
the astronomical library functions.  Only the bare minimum of IDL_ built-in
functions are implemented to support this.

.. _IDL: http://www.harrisgeospatial.com/SoftwareTechnology/IDL.aspx
"""

# Packages may add whatever they like to this file, but
# should keep this content at the top.
# ----------------------------------------------------------------------------
from ._astropy_init import *
# ----------------------------------------------------------------------------

# Enforce Python version check during package import.
# This is the same check as the one at the top of setup.py
import sys

class UnsupportedPythonError(Exception):
    pass

if sys.version_info < tuple((int(val) for val in "2.7".split('.'))):
    raise UnsupportedPythonError("PyDL does not support Python < {}".format(2.7))

if not _ASTROPY_SETUP_:
    # For egg_info test builds to pass, put package imports here.
    from .file_lines import file_lines
    from .median import median
    from .pcomp import pcomp
    from .rebin import rebin
    from .smooth import smooth
    from .uniq import uniq


# Workaround: Numpy 1.14.x changes the way arrays are printed.
try:
    from numpy import set_printoptions
    set_printoptions(legacy='1.13')
except Exception:
    pass


class PydlException(Exception):
    """Base class for exceptions raised in PyDL functions.
    """
    pass

__all__ = ['file_lines', 'median', 'pcomp', 'rebin', 'smooth', 'uniq',
           'PydlException']
