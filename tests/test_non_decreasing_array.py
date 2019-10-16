"""Test non_decreasing_array."""


from hypothesis import given
from hypothesis import event
import hypothesis.strategies as st
import pytest

from algorithms.non_decreasing_array import NonDecreasingArray


funcs = [NonDecreasingArray.is_non_decr_array,
         NonDecreasingArray.is_non_decr_array_2]


@pytest.mark.parametrize('func', funcs)
@pytest.mark.parametrize('input, expected',
                         [([4, 2, 2], True),
                          ([2, 3], True),
                          ([1, 2, 3], True),
                          ([4, 2, 1], False),
                          ([3, 4, 2, 3], False),
                          ([3, 4, 3, 3], True),
                          ([1, 5, 4, 6, 7, 8, 9], True),
                          ([2, 3, 3, 2, 4], True)])
def test_non_decreasing_array(func, input, expected):
    assert func(input) == expected


@pytest.mark.parametrize('func', funcs)
@given(gen_input=st.lists(st.integers(min_value=-3, max_value=3), max_size=6))
def test_non_decreasing_array_generated(func, gen_input):
    expected = False
    for idx, element in enumerate(gen_input):
        exclude_element_list = gen_input.copy()
        exclude_element_list.pop(idx)
        if all(x <= y for x, y in zip(exclude_element_list,
                                      exclude_element_list[1:])):
            expected = True

    if len(gen_input) <= 2:
        expected = True

    actual = func(gen_input)
    event('{}, {}, {}'.format(gen_input, expected, actual))
    assert actual == expected

