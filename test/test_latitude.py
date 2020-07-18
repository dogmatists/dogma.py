#!/usr/bin/env python3
# This is free and unencumbered software released into the public domain.

"""Test cases for the dogma.Latitude class."""

from dogma import Latitude

def test_radians():
    assert(Latitude(2).radians == 2)

if __name__ == '__main__':
    import pytest, sys
    sys.exit(pytest.main([__file__]))
