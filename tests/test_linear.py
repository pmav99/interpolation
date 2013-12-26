#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# file tests/test_linear.py
#
#############################################################################
# Copyright (c) 2013 by Panagiotis Mavrogiorgos
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of source code must retain the above copyright notice,
#   this list of conditions and the following disclaimer.
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
# * Neither the name(s) of the copyright holders nor the names of its
#   contributors may be used to endorse or promote products derived from this
#   software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AS IS AND ANY EXPRESS OR
# IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO
# EVENT SHALL THE COPYRIGHT HOLDERS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA,
# OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
# EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#############################################################################
#
# @license: http://opensource.org/licenses/BSD-3-Clause
# @authors: see AUTHORS.txt

""" Test LinearInterpolation.  """

from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import

import unittest

from nose.tools import assert_almost_equal, assert_raises

from interpolation import LinearInterpolation


def test_zero_length_raises_an_error():
    assert_raises(ValueError, LinearInterpolation, (), ())
    assert_raises(ValueError, LinearInterpolation, (1,), (2,))


def test_arrays_of_different_length_raise_an_error():
    assert_raises(ValueError, LinearInterpolation, (1, 2, 3), (1, 2))
    assert_raises(ValueError, LinearInterpolation, (1, 2), (1, 2, 3))


def test_x_array_in_strictly_ascending_order():
    assert_raises(ValueError, LinearInterpolation, (1, 2, 1), (2, 3, 4))
    assert_raises(ValueError, LinearInterpolation, (2, 1, 2), (2, 3, 4))
    assert_raises(ValueError, LinearInterpolation, (1, 2, 2), (2, 3, 4))
    assert_raises(ValueError, LinearInterpolation, (1, 1, 2), (2, 3, 4))


def test_no_extrapolation():
    table = LinearInterpolation(
        x_index=(1, 2, 3.4, 5.8, 6, 8),
        values=(2, 4, 5.8, 4.3, 4, 6),
        extrapolate=False)

    assert_raises(ValueError, table, 0)
    assert_raises(ValueError, table, 10)


def test_interpolations_table():
    table = LinearInterpolation(
        x_index=(1, 2, 3.4, 5.8, 6, 8),
        values=(2, 4, 5.8, 4.3, 4, 6),
        extrapolate=True)

    assert_almost_equal(table(0), 0)
    assert_almost_equal(table(1), 2)

    assert_almost_equal(table(2.7), 4.9)
    assert_almost_equal(table(4), 5.425)
    assert_almost_equal(table(8), 6)
    assert_almost_equal(table(10), 8)


if __name__ == "__main__":
    unittest.main()
