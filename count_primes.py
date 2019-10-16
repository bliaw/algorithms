"""Count Primes Algorithm."""


import math


class CountPrimes:
    """Count the number of prime numbers less than a non-negative integer.

    https://leetcode.com/problems/count-primes/

    Notes
    -----
    count_primes: brute force.

    count_primes_2: 10x faster than count_primes due to only checking prime vs
    all primes and composites and only checking up to sqrt(number).

    count_primes_3: 10x faster than count_primes_2 due to not needing to
    check for factor at all and just marking out multiples of prime.  The
    next non-marked out number is automatically a prime.
    """

    first_prime = 2

    @staticmethod
    def count_primes(upper_bound_int: int) -> int:
        """Brute force approach checking each number.

        Parameters
        ----------
        upper_bound_int
            Non-inclusive upper bound number.

        Returns
        -------
        Total number of primes < the target number.

        Examples
        --------
        >>> CountPrimes.count_primes(10)
        4

        """
        if upper_bound_int <= CountPrimes.first_prime:
            return 0

        num_primes = 0
        for candidate in range(2, upper_bound_int):
            is_prime = True
            for divisor in range(2, candidate):
                if candidate % divisor == 0:
                    is_prime = False
                    break
            if is_prime:
                num_primes += 1
        return num_primes

    @staticmethod
    def count_primes_2(upper_bound_int: int) -> int:
        """Optimization using the following properties:

         - All natural numbers must contain a prime factor -> we only need to
         check the primes.
         - Only need to check up to sqrt(number) to determine if number is a
         prime.
         """
        if upper_bound_int <= CountPrimes.first_prime:
            return 0

        # Init 2 as first prime number, otherwise no confirmed primes to
        # check against.
        confirmed_primes = [2]
        potential_primes = tuple(range(3, upper_bound_int))

        # Check against only previous prime factors.
        for candidate in potential_primes:
            for factor in confirmed_primes:
                # Mark non-prime once found a prime factor
                if candidate % factor == 0:
                    break
                # Confirm prime once hit sqrt of number
                if factor > math.sqrt(candidate):
                    confirmed_primes.append(candidate)
                    break
        return len(confirmed_primes)

    @staticmethod
    def count_primes_3(upper_bound_int: int) -> int:
        """Optimization by crossing out all multiples of prime factors.

        Can stop checking for primes once we get to sqrt(upper_bound_int).

        https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
        """
        if upper_bound_int <= CountPrimes.first_prime:
            return 0

        # Init numbers so the value matches index fpr easy housekeeping.
        potential_primes = tuple(range(upper_bound_int))
        is_prime = [True] * len(potential_primes)

        # Start checking at the first prime.
        cursor = CountPrimes.first_prime
        is_prime[:CountPrimes.first_prime] = [False] * cursor

        # Mark all multiples of the prime as non-prime.
        while cursor**2 < upper_bound_int:
            if is_prime[cursor]:
                for candidate in range(cursor**2, upper_bound_int, cursor):
                    is_prime[candidate] = False
            cursor += 1
        return sum(is_prime)


if __name__ == '__main__':
    from algorithms.performance import PerfBenchmark
    algos = ['CountPrimes.count_primes',
             'CountPrimes.count_primes_2',
             'CountPrimes.count_primes_3']
    setup_script = 'from algorithms.count_primes import CountPrimes'
    PerfBenchmark.benchmark_algos(algos, setup_script, 100, 1000)
