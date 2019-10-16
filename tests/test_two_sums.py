"""Test for two sums module."""

import collections
import pytest

from algorithms.two_sums import two_sums, two_sums_2, two_sums_3
from algorithms.two_sums import two_sums_II, two_sums_II_2, two_sums_II_3
from algorithms.two_sums import two_sums_IV, two_sums_IV_2
from datastructures.trees import BinarySearchTree



@pytest.mark.skip
@pytest.mark.parametrize('input_array, input_target, expected',
                         [([2, 7, 11, 9], 9, [0, 1]),
                          ([2, 0, 0, 9], 0, [1, 2])])
def test_two_sums(input_array, input_target, expected):
    assert two_sums(input_array, input_target) == expected


@pytest.mark.skip
@pytest.mark.parametrize('input_array, input_target, expected',
                         [([2, 7, 11, 15], 9, [1, 2]),
                          ([0, 0, 0, 0, 0, 0, 1, 9], 10, [7, 8]),
                          ([-1, 0], -1, [1, 2]),
                          ([0, 0, 3, 4], 0, [1, 2]),
                          ([1, 2, 3, 4, 4, 9, 56, 90], 8, [4, 5])])
def test_two_sums_II_3(input_array, input_target, expected):
    assert two_sums_II_3(input_array, input_target) == expected


@pytest.mark.parametrize('input_tree, input_target, expected',
                         [([(5, 5), (3, 3), (6, 6), (2, 2),
                            (4, 4), (7, 7)], 9, True),
                         ([(5, 5), (3, 3), (6, 6), (2, 2),
                            (4, 4), (7, 7)], 28, False),
                          ([(5, 5), (3, 3), (6, 6),
                             (4, 4), (7, 7)], 111, False),
                          ([(1, 1)], 2, False)]
                         )
def test_two_sums_IV_2(input_tree, input_target, expected):
    tree = BinarySearchTree(collections.OrderedDict(input_tree))
    assert two_sums_IV_2(tree._root, input_target) == expected