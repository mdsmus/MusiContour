# -*- coding: utf-8 -*-

import contour.auxiliary as auxiliary
from contour.contour import Contour


def test_permut_csegs():
    cardinality = 3
    fn = auxiliary.permut_csegs(cardinality)
    assert fn == [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0],
                    [2, 0, 1], [2, 1, 0]]


def test_apply_fn():
    assert auxiliary.apply_fn(Contour([0, 1, 2]), 'retrograde') == [2, 1, 0]


def test_absolute_pitches():
    cseg = Contour([1, 4, 2, 3, 0])
    pitches_set = [0, 7, 6, 9, 4]
    assert auxiliary.absolute_pitches(cseg, pitches_set) == [12, 31, 18, 21, 4]


def test_absolute_pitches_permutation():
    cseg = Contour([0, 1, 2])
    pitch_set = [3, 4, 5]
    fn = auxiliary.absolute_pitches_permutation(cseg, pitch_set)
    assert fn == [[3, 4, 5], [3, 5, 16], [4, 15, 17], [4, 5, 15],
                  [5, 15, 16], [5, 16, 27]]


def test_octave_calculator():
    assert auxiliary.octave_calculator(50) == (2, 4)


def test_cseg_string_to_Contour():
    assert auxiliary.cseg_string_to_Contour('< 0 1 2 >') == [0, 1, 2]


def test_note_to_absolute_pitch_from_note_octave():
    assert auxiliary.absolute_pitch_from_note_octave(1, 3) == 37


def test_absolute_pitch_from_str():
    assert auxiliary.absolute_pitch_from_str('d#4') == 51


def test_notes_to_Contour():
    assert auxiliary.notes_to_Contour('c4 d3 e5') == [1, 0, 2]


def test_interval_1():
    n = [1, 5]
    assert auxiliary.interval(n) == 4


def test_interval_2():
    n = [3, 0]
    assert auxiliary.interval(n) == -3


def test_comparison_1():
    n = [1, 4]
    assert auxiliary.comparison(n) == 1


def test_comparison_2():
    n = [5, 0]
    assert auxiliary.comparison(n) == -1


def test_cseg_from_class_number():
    assert auxiliary.cseg_from_class_number(4, 7) == [1, 0, 3, 2]
