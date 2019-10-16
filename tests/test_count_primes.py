"""Test count_primes."""


from hypothesis import given
import hypothesis.strategies as st
import pytest

from algorithms.count_primes import CountPrimes


funcs = [CountPrimes.count_primes,
         CountPrimes.count_primes_2,
         CountPrimes.count_primes_3]


@pytest.mark.parametrize('func', funcs)
@pytest.mark.parametrize('input, expected', [(10, 4),
                                             (1, 0),
                                             (2, 0),
                                             (3, 1),
                                             (4, 2),
                                             (5, 2),
                                             (6, 3),
                                             (102, 26),
                                             (103, 26),
                                             (104, 27)])
def test_count_primes(func, input, expected):
    assert func(input) == expected


@pytest.mark.parametrize('func', funcs)
@given(gen_input=st.integers(max_value=1000))
def test_count_primes_generated(func, gen_input):
    assert func(gen_input) == _brute_force_num_primes(gen_input)


def _brute_force_num_primes(upper_bound_int):
    # Brute force to correctness check for generated inputs.
    if upper_bound_int < 2:
        return 0

    num_primes = 0
    for potential_prime in range(2, upper_bound_int):
        is_prime = True
        for divisor in range(2, potential_prime):
            if potential_prime % divisor == 0:
                is_prime = False
                break
        if is_prime:
            num_primes += 1
    return num_primes
