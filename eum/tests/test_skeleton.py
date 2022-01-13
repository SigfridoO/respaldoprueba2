#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from eum.skeleton import fib

__author__ = "joshuargmx"
__copyright__ = "joshuargmx"
__license__ = "none"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)
