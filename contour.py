#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from itertools import permutations, combinations, izip
from utils import flatten


def __contour_classes_generator_cardinality(cardinality):
    """Generates contour classes like Marvin and Laprade (1987)
    software for one cardinality

    Returns (cardinality, number, contour class).

    'base' stores the c-pitches of a given cardinality.

    'permut' stores all permutations with csegs of a given
    cardinality.

    '__cc_repeat stores prime forms of permut. It may have
    duplicates.

    '_cc_no_repeat' stores enumerated sorted contour class without
    duplicates.
    """

    base = range(cardinality)
    permut = permutations(base, cardinality)
    __cc_repeat = [tuple(Contour(x).prime_form()) for x in permut]
    __cc_no_repeat = enumerate(sorted(list(set(__cc_repeat))))
    contour_classes = [(cardinality, n + 1, x) for n, x in __cc_no_repeat]
    return contour_classes


def contour_classes_generator(cardinality):
    """Generates contour classes like Marvin and Laprade (1987)
    software."""

    card_list = range(2, (cardinality + 1))
    return [__contour_classes_generator_cardinality(c) for c in card_list]


def print_contour_classes(cardinality):
    """Prints contour classes like Marvin and Laprade (1987).

    'cc' stores flatten contour classes of all cardinalities until the
    one given.
    """

    print("C-space segment-classes [based on Marvin and Laprade (1987)]")
    print("{0}\n".format("-" * 60))

    cc = flatten(contour_classes_generator(cardinality))
    card = 0
    for a, b, c in [(a, b, c) for (a, b, c) in cc]:
        if a != card:
            print("\nC-space segment classes for cseg cardinality", a)
            print("\n", " ".ljust(1), "Csegclass".ljust(18),
                  "Prime form".ljust(20), "INT(1)")
            card = a

        csegclass = Contour(c).cseg_visual_printing()
        int_diagonals = Contour(c).internal_diagonals(1)
        str_int_diag = internal_diagonal_print(int_diagonals)
        print(" ".ljust(4), "c {0}-{1}".format(a, b).ljust(16),
              csegclass.ljust(20), str_int_diag.ljust(15))


def double_replace(string):
    """Replaces -1 by -, and 1 by +. Accepts string as input."""

    return string.replace("-1", "-").replace("1", "+")


def replace_list_to_plus_minus(list):
    """Convert a list in a string and replace -1 by -, and 1 by +"""

    return " ".join([double_replace(str(x)) for x in list])


def list_to_string(list):
    """Convert a list in a string.

    Inputs [1, 2, 3] and outputs '1 2 3'
    """

    return " ".join([str(x) for x in list])


def internal_diagonal_print(internal_diagonal):
    """Prints internal diagonal like used in Contour theories:
    < + - + >
    """

    return "< " + replace_list_to_plus_minus(internal_diagonal) + " >"


class Contour():

    def rotation(self, factor=1):
        """Rotates a cseg around a factor.

        factor is optional. Default factor=1.

        'n' is the module of input factor. It's allowed to use factor
        numbers greater than cseg size.
        """

        n = factor % len(self.cseg)
        subset = self.cseg[n:]
        subset.extend(self.cseg[0:n])
        return subset

    def retrograde(self):
        """Returns contour retrograde."""

        self.cseg.reverse()
        return self.cseg

    def inversion(self):
        """Returns contour inversion."""

        maxim = max(self.cseg)
        return [(maxim - cps) for cps in self.cseg]

    def translation(self):
        """Returns the normal form (Marvin 1987) of a given contour.
        It's the same of Friedmann (1985, 1987) contour class (CC)."""

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

        groups = izip(self.cseg, self.cseg[1:])
        return [a for a, b in groups if a != b] + [self.cseg[-1]]

    def subsets(self, n):
        """Returns adjacent and non-adjacent subsets of a given
        contour."""

        cseg = self.cseg
        return sorted([list(x) for x in combinations(cseg, n)])

    def all_subsets(self):
        """Returns adjacent and non-adjacent subsets of a given
        contour."""

        sizes = range(2, len(self.cseg) + 1)
        return flatten([self.subsets(x) for x in sizes])

    def subsets_adj(self, n):
        """Returns adjacent n-elements subsets of a given contour."""

        return [self.cseg[i:i + n] for i in range(len(self.cseg) - (n - 1))]

    def cps_position(self):
        """Returns a tuple with c-pitch and its position for each
        c-pitch of a cseg done."""

        return [(self.cseg[p], p) for p in range(len(self.cseg))]

    def max_min(self, fn):
        """Returns a list with the position of maximum or minimum
        cpitches of a cseg. Maximum or minimum function is defined in
        fn argument.

        'n' stores the number of elements that is evaluated.
        'r' means result.
        """

        n = 3
        cseg_length = len(self.cseg)
        pos = self.cps_position()
        cseg_range = range(cseg_length - (n - 1))

        r = [0]
        [r.append(fn(pos[i:i + n])) for i in cseg_range if fn(pos[i:i + n])]
        r.append(cseg_length - 1)
        return r

    def maxima(self):
        """Returns maxima (Morris, 1993) positions in a cseg."""

        return self.max_min(maximum)

    def minima(self):
        """Returns minima (Morris, 1993) positions in a cseg."""

        return self.max_min(minimum)

    def contour_reduction_algorithm_steps(self):
        """Returns a step from Morris (1993) contour reduction."""

        maxim1 = self.maxima()
        minim1 = self.minima()
        step4 = flatten([maxim1, minim1])
        step4 = Contour(sorted(flatten([maxim1, minim1]))).remove_adjacent()
        return [self.cseg[x] for x in step4]

    def contour_reduction_algorithm(self, n):
        """Returns Morris (1993) contour reduction from a cseg n
        times."""

        for i in xrange(n):
            self = Contour(self.contour_reduction_algorithm_steps())
        return self.cseg

    def contour_interval(self):
        """Returns Friedmann (1985) CI, the distance between one
        element in a CC (normal_form cseg here), and a later element
        as signified by +, - and a number (without + here). For
        example, in cseg = [0, 2, 1], CI(0, 2) = 2, e CI(2, 1) = -1."""

        el1, el2 = self.cseg
        return el2 - el1

    def comparison(self):
        """Returns Morris (1987) comparison [COM(a, b)] for two
        c-pitches.

        This method calls contour_interval(), but in contour theory
        there is no relation between them. This calling reason is only
        to reduce code."""

        delta = self.contour_interval()
        return 0 if abs(delta) == 0 else (delta) / abs(delta)

    def contour_interval_succession(self):
        """Return Friedmann (1985) CIS, a series which indicates the
        order of Contour Intervals in a given CC (normal form cseg
        here)."""

        subsets = self.subsets_adj(2)
        return [Contour([x[0], x[-1]]).contour_interval() for x in subsets]

    def internal_diagonals(self, n):
        """Returns Morris (1987) int_n. The first internal diagonal
        (int_1) is the same of Friedmann (1985, 1987) contour
        adjacency series (CC)."""

        subsets = self.subsets_adj(n + 1)
        return [Contour([x[0], x[-1]]).comparison() for x in subsets]

    def comparison_matrix(self):
        """Returns Morris (1987) a cseg COM-Matrix."""

        size = len(self.cseg)
        m = [[a, b] for a in self.cseg for b in self.cseg]
        n = [m[(i * size):((i + 1) * size)] for i in range(size)]
        return [[Contour(x).comparison() for x in n[r]] for r in range(size)]

    def contour_adjacency_series_vector(self):
        """Returns Friedmann (1985) CASV, a two digit summation of ups
        and downs of a CAS (internal diagonal n=1 here). For example,
        [2, 1] means 2 ups and 1 down.

        'internal_diagonal' stores cseg internal diagonal, n = 1.

        'ups' stores the total number of ups

        'downs' stores the total number of downs
        """

        internal_diagonal = self.internal_diagonals(1)
        ups = sum([(x if x > 0 else 0) for x in internal_diagonal])
        downs = sum([(x if x < 0 else 0) for x in internal_diagonal])
        return [ups, abs(downs)]

    def contour_interval_array(self):
        """Return Friedmann (1985) CIA, an ordered series of numbers
        that indicates the multiplicity of each Contour Interval type
        in a given CC (normal form cseg here). For cseg [0, 1, 3, 2],
        there are 2 instances of type +1 CI, 2 type +2 CI, 1. CIA =
        ([2, 2, 1], [1, 0, 0])

        'up_intervals' and 'down_intervals' store the contour intervals
        that the method counts.

        The loop appends positive elements in ups_list and negative in
        downs_list.

        'ups' and 'downs' stores contour intervals counting for all
        types of positive and negative intervals in the cseg.
        """

        up_intervals = range(1, len(self.cseg))
        down_intervals = [-x for x in up_intervals]
        ups_list = []
        downs_list = []

        for x in combinations(self.cseg, 2):
            y = Contour(x).contour_interval()
            if y > 0:
                ups_list.append(y)
            elif y < 0:
                downs_list.append(y)

        ups = [ups_list.count(x) for x in up_intervals]
        downs = [downs_list.count(x) for x in down_intervals]

        return ups, downs

    def contour_class_vector_i(self):
        """Return Friedmann (1985) CCVI, a two-digit summation of
        degrees of ascent and descent expressed in contour interval
        array. The first digit is the total of products of frequency
        and contour interval types of up contour intervals, and the
        second, of down contour intervals. For example, in CIA([2, 2,
        1], [1, 0, 0], CCVI = [(2 * 1) + (2 * 2) + (1 * 3)], [(1 * 1),
        (2 * 0), (3 * 0)]. So, CCVI = [5, 1].

        'items' stores the contour intervals to be sum.

        'up_list' and 'down_list' stores the up and down contour
        interval frequency lists.

        'up_sum' and 'down_sum' stores the sum of the product of each
        contour interval frequency and contour interval value.
        """

        items = range(1, len(self.cseg))
        up_list, down_list = self.contour_interval_array()
        up_sum = sum([a * b for a, b in izip(up_list, items)])
        down_sum = sum([a * b for a, b in izip(down_list, items)])
        return [up_sum, down_sum]

    def contour_class_vector_ii(self):
        """Return Friedmann (1985) CCVII, a two-digit summation of
        degrees of ascent and descent expressed in contour interval
        array. The first digit is the total of frequency of up contour
        intervals, and the second, of down contour intervals. For
        example, in CIA([2, 2, 1], [1, 0, 0], CCVII = [5, 1]."""

        return [sum(x) for x in self.contour_interval_array()]

    def contour_segment_class(self):
        """Returns contour segment class of a given cseg.

        Output format is: (cardinality, number, cseg_class), like
        (3, 1, (0, 1, 2)).
        """

        prime_form = self.prime_form()
        cseg_classes = flatten(contour_classes_generator(len(self.cseg)))
        for (cardinality, number, cseg_class) in cseg_classes:
            if tuple(prime_form) == cseg_class:
                return cardinality, number, cseg_class

    def cseg_visual_printing(self):
        """Prints cseg like used in Contour theories:
        < 1 3 5 4 >
        """

        return "< " + list_to_string(self.cseg) + " >"

    def comparison_matrix_printing(self):
        """Prints comparison matrix like used in Contour theories:

        . | 0 2 1
        ---------
        0 | 0 + +
        2 | - 0 +
        1 | - + 0

        'str_matrix' stores a list with comparison matrix complete
        lines.
        """

        hline = "{0}".format("-" * ((len(self.cseg) * 2) + 3))
        cseg_printing = list_to_string(self.cseg)
        com_matrix = self.comparison_matrix()
        str_matrix = [(str(self.cseg[i]) + " | " + \
                       replace_list_to_plus_minus(line)) \
                      for (i, line) in enumerate(com_matrix)]
        half_matrix_1 = "  | " + cseg_printing + "\n" + hline + "\n"
        half_matrix_2 = "".join([x + "\n" for x in str_matrix])
        return half_matrix_1 + half_matrix_2

    def __init__(self, cseg):
        self.cseg = cseg


class Contour_subsets():

    def subsets_count(self):
        """Counts contour subset classes with n elements."""

        tuples = [tuple(x) for x in self.subsets]
        contour_type = sorted(list(set(tuples)))
        counted_contours = [[x, tuples.count(x)] for x in contour_type]
        return sorted(counted_contours, key=lambda x: x[1], reverse=True)

    def normal_form_subsets(self):
        """Outputs normal form of a list of subsets."""

        return [Contour(x).translation() for x in self.subsets]

    def prime_form_subsets(self):
        """Outputs normal form of a list of subsets."""

        return [Contour(x).prime_form() for x in self.subsets]

    def normal_form_subsets_count(self):
        """Counts subset prime forms with n elements."""

        normal_form = self.normal_form_subsets()
        return Contour_subsets(normal_form).subsets_count()

    def prime_form_subsets_count(self):
        """Counts subset prime forms with n elements."""

        prime_form = self.prime_form_subsets()
        return Contour_subsets(prime_form).subsets_count()

    def __init__(self, subsets):
        self.subsets = subsets


def ri_identity_test(cseg):
    """Returns 1 if cseg have identity under retrograde inversion."""

    return 1 if cseg == Contour(Contour(cseg).retrograde()).inversion() else 0


def maximum(dur_list):
    """Returns the maximum (Morris, 1993) position of a three
    c-pitches set. The input data is a list of three tuples. Each
    tuple has the c-pitch and its position. """

    (el1, p1), (el2, p2), (el3, p3) = dur_list
    return p2 if el2 >= el1 and el2 >= el3 else ''


def minimum(dur_list):
    """Returns the minimum (Morris, 1993) position of a three
    c-pitches set. The input data is a list of three tuples. Each
    tuple has the c-pitch and its position. """

    (el1, p1), (el2, p2), (el3, p3) = dur_list
    return p2 if el2 <= el1 and el2 <= el3 else ''


def remove_duplicate_tuples(list_of_tuples):
    """Removes tuples that the first item is repeated in adjacent
    tuples. The removed tuple is the second."""

    prev = None
    tmp = []
    for a, b in list_of_tuples:
        if a != prev:
            tmp.append((a, b))
            prev = a
    return tmp


def __intern_diagon_sim(cseg1, cseg2, n):
    """Returns the number of positions where cseg1 and cseg2 have the
    same value in a n-internal diagonal."""

    c1, c2 = Contour(cseg1), Contour(cseg2)
    d1, d2 = c1.internal_diagonals(n), c2.internal_diagonals(n)
    length = len(d1)
    return sum([(1 if d1[i] == d2[i] else 0) for i in range(length)])


def cseg_similarity(cseg1, cseg2):
    """Returns Marvin and Laprade (1987) Csim(a, b). It's a contour
    similarity function that measures similarity between two csegs of
    the same cardinality. The maximum similarity is 1, and minimum is
    0.

    'd' means the number of internal diagonals.

    'triang_pos' is the number of positions in triangle above the zero
    diagonal.

    'similar pos' is the number of positions where cseg1 and cseg2
    have the same value. This variable is calculated with the private
    method __intern_diagon_sim().
    """

    d = range(len(cseg1))
    d.remove(0)
    triangle_pos = sum(d)
    similar_pos = sum([__intern_diagon_sim(cseg1, cseg2, n) for n in d])
    return similar_pos / float(triangle_pos)


class Internal_diagonal():

    def csegs(self, diagonal=1):
        """Returns all csegs in normal form that have the given
        internal diagonal.

        >>> Internal_diagonal([-1, 1, 1]).csegs
        [[1, 0, 2, 3], [2, 0, 1, 3], [3, 0, 1, 2]]
        """

        size = len(self.internal_diagonal) + diagonal
        base_contour = range(size)
        permut = permutations(base_contour)
        int_d_permut = [[Contour(list(x)).internal_diagonals(diagonal), list(x)] for x in permut]
        result = []
        [result.append(y[1]) for y in int_d_permut if y[0] == self.internal_diagonal]
        return result

    def rotation(self, factor=1):
        """Rotates an internal diagonal around a factor.

        factor is optional. Default factor=1.

        'n' is the module of input factor. It's allowed to use factor
        numbers greater than internal diagonal size.
        """

        n = factor % len(self.internal_diagonal)
        subset = self.internal_diagonal[n:]
        subset.extend(self.internal_diagonal[0:n])
        return subset

    def retrograde(self):
        """Returns internal diagonal retrograde."""

        self.internal_diagonal.reverse()
        return self.internal_diagonal

    def inversion(self):
        """Returns Internal diagonal inversion.

        >>> Internal_diagonal([-1, 1, 1]).inversion
        [1, -1, -1]
        """

        return [(x * -1) for x in self.internal_diagonal]

    def subsets(self, n):
        """Returns adjacent and non-adjacent subsets of a given
        contour."""

        int_d = self.internal_diagonal
        return sorted([list(x) for x in combinations(int_d, n)])

    def all_subsets(self):
        """Returns adjacent and non-adjacent subsets of a given
        contour."""

        sizes = range(2, len(self.internal_diagonal) + 1)
        return flatten([self.subsets(x) for x in sizes])

    def subsets_adj(self, n):
        """Returns adjacent n-elements subsets of a given contour."""

        int_d = self.internal_diagonal
        return [int_d[i:i + n] for i in range(len(int_d) - (n - 1))]

    def __init__(self, internal_diagonal):
        self.internal_diagonal = internal_diagonal
