#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import itertools as i
import utils as u


class Contour():

    def retrograde(self):
        """Returns contour retrograde."""

        self.cseg.reverse()
        return self.cseg

    def inversion(self):
        """Returns contour inversion."""

        maxim = max(self.cseg)
        minim = min(self.cseg)
        axis = ((maxim - minim) / 2.0 + minim)
        return [int("%d" % ((axis * 2) - x)) for x in self.cseg]

    def translation(self):
        """Returns the normal form of a given contour."""

        sorted_contour = sorted(list(set(self.cseg)))
        return [sorted_contour.index(x) for x in self.cseg]

    def prime_form(self):
        """Returns the prime form of a given contour."""

        length = len(self.cseg)
        self.cseg = self.translation()
        if ((length - 1) - self.cseg[-1]) < self.cseg[0]:
            self.cseg = self.inversion()
        else:
            self.cseg
        if self.cseg[-1] < self.cseg[0]:
            self.cseg = self.retrograde()
        else:
            self.cseg
        return self.cseg

    def remove_adjacent(self):
        """Removes adjacent elements from a list."""

        return [a for a, b in i.izip(self.cseg, self.cseg[1:])
                if a != b] + [self.cseg[-1]]

    def contour_subsets(self, n):
        """Returns adjacent n-elements subsets of a given contour."""

        return [self.cseg[i:i + n] for i in range((len(self.cseg) - (n - 1)))]

    def local(self):
        """Returns a tuple with c-pitches and positions."""

        return [(self.cseg[p], p) for p in range(len(self.cseg))]

    def maxima(self):
        """Returns maxima positions in a cseg."""

        length = len(self.cseg)
        l = self.local()
        maxima = [maximum(l[i:i + 3])
                  for i in range(length - (3 - 1))
                  if maximum(l[i:i + 3])]
        maxima.insert(0, 0)
        maxima.append(length - 1)
        return maxima

    def minima(self):
        """Returns minima positions in a list."""

        length = len(self.cseg)
        l = self.local()
        minima = [minimum(l[i:i + 3])
                  for i in range(length - (3 - 1))
                  if minimum(l[i:i + 3])]
        minima.insert(0, 0)
        minima.append(length - 1)
        return minima

    def contour_reduction_algorithm(self):
        """Returns Morris (1993) contour reduction from a cseg."""

        ma = self.maxima()
        mi = self.minima()
        r = u.flatten([ma, mi])
        r = Contour(sorted(u.flatten([ma, mi]))).remove_adjacent()
        return [self.cseg[x] for x in r]

    def com(self):
        """Returns Morris (1987) comparison [COM(a, b)] for two
        c-pitches."""

        it = iter(self.cseg)
        el1 = it.next()
        el2 = it.next()
        if abs(el2 - el1) == 0:
            r = 0
        else:
            r = (el2 - el1) / abs(el2 - el1)
        return r

    def int(self, n):

        """Returns Morris (1987) int_n."""

        subsets = self.contour_subsets(n + 1)
        return [Contour([x[0], x[-1]]).com() for x in subsets]

    def __init__(self, c):
        self.cseg = c


class Contour_subsets():

    def subsets_count(self):
        """Counts contour subset classes with n elements."""

        tuples = [tuple(x) for x in self.ss]
        contour_type = sorted(list(set(tuples)))
        counted_contours = [[x, tuples.count(x)] for x in contour_type]
        return sorted(counted_contours, key=lambda x: x[1], reverse=True)

    def normal_form_subsets(self):
        """Outputs normal form of a list of subsets."""

        return [Contour(x).translation() for x in self.ss]

    def prime_form_subsets(self):
        """Outputs normal form of a list of subsets."""

        return [Contour(x).prime_form() for x in self.ss]

    def normal_form_subsets_count(self):
        """Counts subset prime forms with n elements."""

        normal_form = self.normal_form_subsets()
        return Contour_subsets(normal_form).subsets_count()

    def prime_form_subsets_count(self):
        """Counts subset prime forms with n elements."""

        prime_form = self.prime_form_subsets()
        return Contour_subsets(prime_form).subsets_count()

    def __init__(self, subsets):
        self.ss = subsets


def maximum(dur_list):
    """Returns the maximum (Morris, 1993) position of a three
    c-pitches set. The input data is a list of three tuples. Each
    tuple has the c-pitch and its position. """

    it = iter(dur_list)
    el1, p1 = it.next()
    el2, p2 = it.next()
    el3, p3 = it.next()
    if el2 >= el1 and el2 >= el3:
        return p2
    else:
        return ''


def minimum(dur_list):
    """Returns the minimum (Morris, 1993) position of a three
    c-pitches set. The input data is a list of three tuples. Each
    tuple has the c-pitch and its position. """

    it = iter(dur_list)
    el1, p1 = it.next()
    el2, p2 = it.next()
    el3, p3 = it.next()
    if el2 <= el1 and el2 <= el3:
        return p2
    else:
        return ''
