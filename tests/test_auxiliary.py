# -*- coding: utf-8 -*-

import contour.auxiliary as aux
from contour.contour import Contour

def test_subsets_count():
    n = [[2, 8, 12, 9], [8, 12, 9, 5], [12, 9, 5, 7], [9, 5, 7, 3],
         [5, 7, 3, 12], [7, 3, 12, 3], [3, 12, 3, 7]]
    assert aux.subsets_count(n) == [[(2, 8, 12, 9), 1],
                                    [(3, 12, 3, 7), 1],
                                    [(5, 7, 3, 12), 1],
                                    [(7, 3, 12, 3), 1],
                                    [(8, 12, 9, 5), 1],
                                    [(9, 5, 7, 3), 1],
                                    [(12, 9, 5, 7), 1]]


def test_normal_form_subsets():
    n = [[2, 8, 12, 9], [8, 12, 9, 5], [12, 9, 5, 7], [9, 5, 7, 3],
         [5, 7, 3, 12], [7, 3, 12, 3], [3, 12, 3, 7]]
    assert aux.normal_form_subsets(n) == [[0, 1, 3, 2],
                                          [1, 3, 2, 0],
                                          [3, 2, 0, 1],
                                          [3, 1, 2, 0],
                                          [1, 2, 0, 3],
                                          [1, 0, 2, 0],
                                          [0, 2, 0, 1]]


def test_prime_form_subsets():
    n = [[2, 8, 12, 9], [8, 12, 9, 5], [12, 9, 5, 7], [9, 5, 7, 3],
         [5, 7, 3, 12], [7, 3, 12, 3], [3, 12, 3, 7]]
    assert aux.prime_form_subsets(n) == [Contour([0, 1, 3, 2]),
                                         Contour([0, 2, 3, 1]),
                                         Contour([0, 1, 3, 2]),
                                         Contour([0, 2, 1, 3]),
                                         Contour([0, 3, 1, 2]),
                                         [Contour([2, 0, 3, 1]), Contour([2, 1, 3, 0])],
                                         [Contour([0, 3, 1, 2]), Contour([1, 3, 0, 2])]]


def test_normal_form_subsets_count():
    n = [[2, 8, 12, 9], [8, 12, 9, 5], [12, 9, 5, 7], [9, 5, 7, 3],
         [5, 7, 3, 12], [7, 3, 12, 3], [3, 12, 3, 7]]
    assert aux.normal_form_subsets_count(n) == [[(0, 1, 3, 2), 1],
                                                [(0, 2, 0, 1), 1],
                                                [(1, 0, 2, 0), 1],
                                                [(1, 2, 0, 3), 1],
                                                [(1, 3, 2, 0), 1],
                                                [(3, 1, 2, 0), 1],
                                                [(3, 2, 0, 1), 1]]


def test_prime_form_subsets_count():
    n = [[2, 8, 12, 9], [8, 12, 9, 5], [12, 9, 5, 7], [9, 5, 7, 3],
         [5, 7, 3, 12], [7, 3, 12, 3], [3, 12, 3, 7]]
    assert aux.prime_form_subsets_count(n) == [[(0, 1, 3, 2), 2],
                                               [(0, 2, 0, 1), 2],
                                               [(0, 2, 1, 3), 1],
                                               [(0, 2, 3, 1), 1],
                                               [(0, 3, 1, 2), 1]]


def test_absolute_pitches():
    cseg = Contour([1, 4, 2, 3, 0])
    pitches_set = [0, 7, 6, 9, 4]

    assert aux.absolute_pitches(cseg, pitches_set) == [12, 31, 18, 21, 4]
