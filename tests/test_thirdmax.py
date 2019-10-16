"""Test thirdmax."""


from hypothesis import given
from hypothesis import strategies as st
import pytest

from algorithms.thirdmax import ThirdMax


funcs = [ThirdMax.thirdmax,
         ThirdMax.thirdmax_2]


@pytest.mark.parametrize('func', funcs)
@pytest.mark.parametrize('input, expected', [([1, 2, 3, 4, 5], 3),
                                             ([1], 1),
                                             ([1, 1, 1, 1, 1, 2], 2),
                                             ([-1, -2, -3, 0, 1, 2], 0)])
def test_thirdmax(func, input, expected):
    assert func(input) == expected


@pytest.mark.parametrize('func', funcs)
@given(gen_input=st.lists(st.integers(), min_size=1, max_size=10000))
def test_thirdmax_generated(func, gen_input):
    unique = list(set(gen_input))
    if len(unique) <= 2:
        expected = max(unique)
    else:
        unique.sort()
        expected = unique[-3]
    assert func(gen_input) == expected


@pytest.mark.parametrize('func', funcs)
def test_thirdmax_benchmark(func):
    import random
    from algorithms.performance import PerfBenchmark

    setup_script = 'from algorithms.thirdmax import ThirdMax'

    # Check to make sure algo is O(n)
    short_input = [random.choice(range(10000)) for _ in range(10)]
    long_input = [random.choice(range(10000)) for _ in range(100000)]
    PerfBenchmark.benchmark_algos(['ThirdMax.'+func.__name__],
                                  setup_script,
                                  100,
                                  short_input)
    PerfBenchmark.benchmark_algos(['ThirdMax.'+func.__name__],
                                  setup_script,
                                  100,
                                  long_input)
    assert True
