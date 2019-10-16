"""Test rotate_array."""


from hypothesis import assume
from hypothesis import given
from hypothesis import strategies as st
import pytest

from algorithms.rotate_array import RotateArray


@pytest.mark.parametrize('input, input_k, expected',
                         [([1, 2], 11, [2, 1]),
                          ([-1, -100, 3, 99], 0, [-1, -100, 3, 99]),
                          ([-1, -100, 3, 99], 2, [3, 99, -1, -100]),
                          ([1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4]),
                          ([1, 0], 1, [0, 1])
                          ])
def test_rotate_array(input, input_k, expected):
    nums = input
    RotateArray.rotate(nums, input_k)
    assert nums == expected


@given(gen_input=st.lists(st.integers()), gen_input_k=st.integers(max_value=10000))
def test_rotate_array_gen(gen_input, gen_input_k):
    assume (gen_input_k < len(gen_input))

    # Calculate expected results.
    gen_input_copy = gen_input.copy()  # ops are in-place
    length = len(gen_input)
    # Avoid mod by 0
    if length > 0:
        expected = [gen_input_copy[(idx - gen_input_k) % length] for idx in range(length)]
    else:
        expected = gen_input_copy

    nums = gen_input
    RotateArray.rotate(nums, gen_input_k)
    assert  nums == expected
