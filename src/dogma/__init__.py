# This is free and unencumbered software released into the public domain.

"""Dogma for Python."""

import sys

assert sys.version_info >= (3, 6), "Dogma requires Python 3.6+"

from .angle import Angle

__all__ = [
    'Angle',
]
