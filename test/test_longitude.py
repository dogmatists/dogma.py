#!/usr/bin/env python3
# This is free and unencumbered software released into the public domain.

"""Test cases for the dogma.Longitude class."""

from dogma import Longitude

def test_radians():
    assert(Longitude(2).radians == 2)

if __name__ == '__main__':
    import pytest, sys
    sys.exit(pytest.main([__file__]))
