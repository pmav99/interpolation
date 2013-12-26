#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# file interpolation/linear.py
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

from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import

from bisect import bisect_left


class LinearInterpolation(object):
    def __init__(self, x_index, values, extrapolate=True):
        # sanity check
        length = len(x_index)
        if length != len(values):
            raise ValueError("Arrays must be of equal length! index:<%r>, values:<%r>" % (x_index, values))
        if length < 2:
            raise ValueError("Arrays must have length at least 2.")
        if any(x2 - x1 <= 0 for x1, x2 in zip(x_index, x_index[1:])):
            raise ValueError("index must be in strictly ascending order!")

        # attributes
        self.x_index = x_index
        self.values = values
        self.length = length
        self.extrapolate = extrapolate

        # precalculate slopes
        intervals = zip(x_index, x_index[1:], values, values[1:])
        self.slopes = [(y2 - y1) / (x2 - x1) for x1, x2, y1, y2 in intervals]

    def __call__(self, x):
        i = bisect_left(self.x_index, x) - 1
        if self.extrapolate:
            if i == -1:
                i = 0
            elif i == self.length - 1:
                i = -1
        else:
            if i == -1 or i == self.length - 1:
                raise ValueError("Extrapolation not allowed!")

        return self.values[i] + self.slopes[i] * (x - self.x_index[i])
