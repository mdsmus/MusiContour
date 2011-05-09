# -*- coding: utf-8 -*-

import contour.contour as contour
from contour.contour import Contour
import py


def test_build_classes_card():
    fn = contour.build_classes_card
    assert fn(4) == [(4, 1, (0, 1, 2, 3), True), (4, 2, (0, 1, 3, 2), False),
                     (4, 3, (0, 2, 1, 3), True), (4, 4, (0, 2, 3, 1), False),
                     (4, 5, (0, 3, 1, 2), False), (4, 6, (0, 3, 2, 1), False),
                     (4, 7, (1, 0, 3, 2), True), (4, 8, (1, 3, 0, 2), True)]


def test_build_classes():
    fn = contour.build_classes
    assert fn(4) == [[(2, 1, (0, 1), True)],
                     [(3, 1, (0, 1, 2), True), (3, 2, (0, 2, 1), False)],
                     [(4, 1, (0, 1, 2, 3), True), (4, 2, (0, 1, 3, 2), False),
                      (4, 3, (0, 2, 1, 3), True), (4, 4, (0, 2, 3, 1), False),
                      (4, 5, (0, 3, 1, 2), False), (4, 6, (0, 3, 2, 1), False),
                      (4, 7, (1, 0, 3, 2), True), (4, 8, (1, 3, 0, 2), True)]]


def test_contour_class():
    assert contour.contour_class(6, 117) == Contour([0, 5, 4, 2, 1, 3])


def test_subsets_grouped():
    n = {(0, 1, 3, 2): [[0, 1, 4, 2]],
         (0, 2, 1, 3): [[0, 3, 1, 4]],
         (0, 2, 3, 1): [[0, 3, 4, 2]],
         (0, 3, 1, 2): [[0, 3, 1, 2]],
         (1, 3, 0, 2): [[3, 1, 4, 2]]}
    assert contour.subsets_grouped(n, "prime") == \
           'Prime form < 0 1 3 2 > (1)\n< 0 1 4 2 >\n' + \
           'Prime form < 0 2 1 3 > (1)\n< 0 3 1 4 >\n' + \
           'Prime form < 0 2 3 1 > (1)\n< 0 3 4 2 >\n' + \
           'Prime form < 0 3 1 2 > (1)\n< 0 3 1 2 >\n' + \
           'Prime form < 1 3 0 2 > (1)\n< 3 1 4 2 >'


def test_rotation_1():
    cseg = Contour([1, 4, 9, 9, 2, 1])
    assert cseg.rotation() == [4, 9, 9, 2, 1, 1]


def test_rotation_2():
    cseg = Contour([1, 4, 9, 9, 2, 1])
    assert cseg.rotation(1) == [4, 9, 9, 2, 1, 1]


def test_rotation_3():
    cseg = Contour([1, 4, 9, 9, 2, 1])
    assert cseg.rotation(2) == [9, 9, 2, 1, 1, 4]


def test_rotation_4():
    cseg = Contour([1, 4, 9, 9, 2, 1])
    assert cseg.rotation(20) == [9, 9, 2, 1, 1, 4]


def test_retrograde():
    cseg = Contour([1, 4, 9, 9, 2, 1])
    assert cseg.retrograde() == [1, 2, 9, 9, 4, 1]


def test_inversion():
    cseg = Contour([1, 4, 9, 9, 2, 1])
    assert cseg.inversion() == [8, 5, 0, 0, 7, 8]


def test_translation():
    cseg = Contour([1, 4, 9, 9, 2, 1])
    assert cseg.translation() == [0, 2, 3, 3, 1, 0]


def test_prime_form_marvin_laprade_1():
    cseg = Contour([1, 4, 9, 2])
    assert cseg.prime_form_marvin_laprade() == [0, 2, 3, 1]


def test_prime_form_marvin_laprade_2():
    cseg = Contour([5, 7, 9, 1])
    assert cseg.prime_form_marvin_laprade() == [0, 3, 2, 1]


def test_prime_form_marvin_laprade_2():
    cseg = Contour([5, 7, 9, 1])
    assert cseg.prime_form_marvin_laprade() == [0, 3, 2, 1]


def test_prime_form_marvin_laprade_3():
    cseg = Contour([0, 2, 1, 3, 4])
    assert cseg.prime_form_marvin_laprade() == [0, 2, 1, 3, 4]


def test_prime_form_marvin_laprade_5():
    cseg = Contour([0, 1, 2, 1, 2])
    assert cseg.prime_form_marvin_laprade() == [[0, 1, 3, 2, 4], [0, 2, 4, 1, 3]]


def test_prime_form_sampaio_1():
    cseg = Contour([1, 4, 9, 2])
    assert cseg.prime_form_sampaio() == [0, 2, 3, 1]


def test_prime_form_sampaio_2():
    cseg = Contour([5, 7, 9, 1])
    assert cseg.prime_form_sampaio() == [0, 3, 2, 1]


def test_prime_form_sampaio_2():
    cseg = Contour([5, 7, 9, 1])
    assert cseg.prime_form_sampaio() == [0, 3, 2, 1]


def test_prime_form_sampaio_3():
    cseg = Contour([0, 2, 1, 3, 4])
    assert cseg.prime_form_sampaio() == [0, 1, 3, 2, 4]


def test_prime_form_sampaio_5():
    cseg = Contour([0, 1, 2, 1, 2])
    assert cseg.prime_form_sampaio() == [[0, 1, 3, 2, 4], [0, 1, 4, 2, 3],
                                         [0, 2, 3, 1, 4], [0, 2, 4, 1, 3]]


def test_unique_prime_form_test_1():
    cseg = Contour([0, 2, 1, 3, 4])
    algorithm = "prime_form_marvin_laprade"
    assert cseg.unique_prime_form_test(algorithm) == False


def test_unique_prime_form_test_2():
    cseg = Contour([0, 2, 1, 3, 4])
    algorithm = "prime_form_sampaio"
    assert cseg.unique_prime_form_test(algorithm) == True


def test_subsets_1():
    cseg = Contour([2, 8, 12, 9])
    assert cseg.subsets(2) == [[2, 8], [2, 9], [2, 12], [8, 9], [8, 12],
                               [12, 9]]


def test_subsets_2():
    cseg = Contour([2, 8, 12, 9])
    assert cseg.subsets(3) == [[2, 8, 9], [2, 8, 12], [2, 12, 9], [8, 12, 9]]


def test_subsets_prime():
    cseg = Contour([0, 3, 1, 4, 2])
    assert cseg.subsets_prime(4) == {(0, 1, 3, 2): [[0, 1, 4, 2]],
                                     (0, 2, 1, 3): [[0, 3, 1, 4]],
                                     (0, 2, 3, 1): [[0, 3, 4, 2]],
                                     (0, 3, 1, 2): [[0, 3, 1, 2]],
                                     (1, 3, 0, 2): [[3, 1, 4, 2]]}


def test_subsets_normal():
    cseg = Contour([0, 3, 1, 4, 2])
    assert cseg.subsets_normal(4) == {(0, 1, 3, 2): [[0, 1, 4, 2]],
                                      (0, 2, 1, 3): [[0, 3, 1, 4]],
                                      (0, 2, 3, 1): [[0, 3, 4, 2]],
                                      (0, 3, 1, 2): [[0, 3, 1, 2]],
                                      (2, 0, 3, 1): [[3, 1, 4, 2]]}


def test_all_subsets():
    cseg = Contour([2, 8, 12, 9])
    assert cseg.all_subsets() == [[2, 8], [2, 9], [2, 12], [8, 9], [8, 12],
                                  [12, 9], [2, 8, 9], [2, 8, 12], [2, 12, 9],
                                  [8, 12, 9], [2, 8, 12, 9]]


def test_all_subsets_prime():
    cseg = Contour([2, 8, 12])
    assert cseg.all_subsets_prime() == {(0, 1): [[2, 8], [2, 12], [8, 12]],
                                        (0, 1, 2): [[2, 8, 12]]}


def test_all_subsets_normal():
    cseg = Contour([2, 8, 7])
    assert cseg.all_subsets_normal() == {(0, 1): [[2, 7], [2, 8]],
                                         (0, 2, 1): [[2, 8, 7]],
                                         (1, 0): [[8, 7]]}


def test_subsets_adj():
    cseg = Contour([2, 8, 12, 9, 5, 7, 3, 12, 3, 7])
    assert cseg.subsets_adj(4) == [[2, 8, 12, 9], [8, 12, 9, 5], [12, 9, 5, 7],
                                   [9, 5, 7, 3], [5, 7, 3, 12], [7, 3, 12, 3],
                                   [3, 12, 3, 7]]


def test_cps_position():
    cseg = Contour([2, 8, 12, 9, 5, 7, 3, 12, 3, 7])
    assert cseg.cps_position() == [(2, 0), (8, 1), (12, 2), (9, 3), (5, 4),
                                   (7, 5), (3, 6), (12, 7), (3, 8), (7, 9)]


def test_reduction_algorithm_1():
    cseg = Contour([0, 4, 3, 2, 5, 5, 1])
    assert cseg.reduction_algorithm() == [[0, 2, 1], 2]


def test_reduction_algorithm_2():
    cseg = Contour([7, 10, 9, 0, 2, 3, 1, 8, 6, 2, 4, 5])
    assert cseg.reduction_algorithm() == [[2, 3, 0, 1], 3]


def test_maxima():
    n = [(0, 0), (1, 1), (3, 2), (2, 3), (4, 4)]
    assert contour.maxima(n) == [(0, 0), (3, 2), (4, 4)]


def test_minima():
    n = [(0, 0), (1, 1), (3, 2), (2, 3), (4, 4)]
    assert contour.minima(n) == [(0, 0), (2, 3), (4, 4)]


def test_contour_rotation_classes():
    assert contour.contour_rotation_classes(4) == [[0, 1, 2, 3],
                                                   [0, 1, 3, 2],
                                                   [0, 2, 1, 3]]


def test_interval_succession():
    cseg = Contour([0, 1, 3, 2])
    assert cseg.interval_succession() == [1, 2, -1]


def test_internal_diagonals_1():
    cseg = Contour([0, 2, 3, 1])
    n = 1
    assert cseg.internal_diagonals(n) == [1, 1, -1]


def test_internal_diagonals_2():
    cseg = Contour([0, 2, 3, 1])
    n = 2
    assert cseg.internal_diagonals(n) == [1, -1]


def test_internal_diagonals_3():
    cseg = Contour([1, 0, 4, 3, 2])
    n = 1
    assert cseg.internal_diagonals(n) == [-1, 1, -1, -1]


def test_internal_diagonals_4():
    cseg = Contour([1, 0, 4, 3, 2])
    n = 2
    assert cseg.internal_diagonals(n) == [1, 1, -1]


def test_comparison_matrix_1():
    cseg = Contour([0, 2, 3, 1])
    assert cseg.comparison_matrix() == [[0, 2, 3, 1], [0, 1, 1, 1], [-1, 0, 1, -1],
                                        [-1, -1, 0, -1], [-1, 1, 1, 0]]


def test_comparison_matrix_2():
    cseg = Contour([1, 2, 3, 0, 3, 1])
    assert cseg.comparison_matrix() == [[1, 2, 3, 0, 3, 1],
                                        [0, 1, 1, -1, 1, 0],
                                        [-1, 0, 1, -1, 1, -1],
                                        [-1, -1, 0, -1, 0, -1],
                                        [1, 1, 1, 0, 1, 1],
                                        [-1, -1, 0, -1, 0, -1],
                                        [0, 1, 1, -1, 1, 0]]


def test_adjacency_series_vector_1():
    cseg = Contour([0, 2, 3, 1])
    assert cseg.adjacency_series_vector() == [2, 1]


def test_adjacency_series_vector_2():
    cseg = Contour([1, 2, 3, 0, 3, 1])
    assert cseg.adjacency_series_vector() == [3, 2]


def test_interval_array():
    cseg = Contour([0, 1, 3, 2])
    assert cseg.interval_array() == ([2, 2, 1], [1, 0, 0])


def test_class_vector_i():
    cseg = Contour([0, 1, 3, 2])
    assert cseg.class_vector_i() == [9, 1]


def test_class_vector_ii():
    cseg = Contour([0, 1, 3, 2])
    assert cseg.class_vector_ii() == [5, 1]


def test_class_index_i():
    cseg = Contour([0, 1, 3, 2])
    assert cseg.class_index_i() == 0.9


def test_class_index_ii():
    cseg = Contour([0, 1, 3, 2])
    assert cseg.class_index_ii() == 5.0 / 6


def test_segment_class_1():
    cseg = Contour([2, 1, 4])
    assert cseg.segment_class() == (3, 2, [0, 2, 1], False)


def test_segment_class_2():
    cseg = Contour([3, 1, 0])
    assert cseg.segment_class() == (3, 1, [0, 1, 2], True)


def test_ri_identity_test_1():
    cseg = Contour([0, 1, 3, 2])
    assert cseg.ri_identity_test() == False


def test_ri_identity_test():
    cseg = Contour([1, 0, 3, 2])
    assert cseg.ri_identity_test() == True


def test_symmetry_index_1():
    cseg = Contour([1, 0, 3, 2])
    assert cseg.symmetry_index() == 1


def test_symmetry_index_2():
    cseg = Contour([0, 2, 1])
    assert cseg.symmetry_index() == 0


def test_symmetry_index_3():
    cseg = Contour([0, 1, 3, 4, 2, 5, 6])
    assert cseg.symmetry_index() == 0.5


def test_class_representatives():
    cseg = Contour([0, 1, 3, 2])
    assert cseg.class_representatives() == [[0, 1, 3, 2], [3, 2, 0, 1],
                                            [2, 3, 1, 0], [1, 0, 2, 3]]


def test_class_four_forms():
    cseg = Contour([0, 1, 3, 2])
    assert cseg.class_four_forms() == [[0, 1, 3, 2], [3, 2, 0, 1],
                                       [2, 3, 1, 0], [1, 0, 2, 3]]


def test_all_rotations_1():
    cseg = Contour([0, 1, 2])
    assert cseg.all_rotations() == [[0, 1, 2], [1, 2, 0], [2, 0, 1], [0, 1, 2]]


def test_all_rotations_2():
    cseg = Contour([0, 3, 1, 2])
    assert cseg.all_rotations() == [[0, 3, 1, 2], [3, 1, 2, 0], [1, 2, 0, 3],
                                    [2, 0, 3, 1], [0, 3, 1, 2]]


def test_rotated_representatives_1():
    cseg = Contour([0, 1, 2])
    assert cseg.rotated_representatives() == [[0, 1, 2], [0, 2, 1], [1, 0, 2],
                                              [1, 2, 0], [2, 0, 1], [2, 1, 0]]


def test_rotated_representatives_2():
    cseg = Contour([0, 3, 1, 2])
    assert cseg.rotated_representatives() == [[0, 2, 1, 3], [0, 3, 1, 2],
                                              [1, 2, 0, 3], [1, 3, 0, 2],
                                              [2, 0, 3, 1], [2, 1, 3, 0],
                                              [3, 0, 2, 1], [3, 1, 2, 0]]


def test_prime_form_algorithm_test_1():
    algorithm = "prime_form_marvin_laprade"
    assert contour.prime_form_algorithm_test(4, algorithm) == []


def test_prime_form_algorithm_test_2():
    algorithm = "prime_form_marvin_laprade"
    fn = contour.prime_form_algorithm_test(5, algorithm)
    assert fn == [[(5, 3), [0, 1, 3, 2, 4], [0, 2, 1, 3, 4]],
                  [(5, 8), [0, 2, 3, 1, 4], [0, 3, 1, 2, 4]],
                  [(5, 25), [1, 0, 4, 2, 3], [1, 2, 0, 4, 3]],
                  [(5, 27), [1, 2, 4, 0, 3], [1, 4, 0, 2, 3]]]


def test_prime_form_algorithm_test_3():
    algorithm = "prime_form_sampaio"
    assert contour.prime_form_algorithm_test(6, algorithm) == []
