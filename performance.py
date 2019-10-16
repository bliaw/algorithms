"""Utility functions for optimizing performance."""


from timeit import timeit
from typing import List


class PerfBenchmark:
    """Benchmarking utility."""

    @staticmethod
    def benchmark_algos(algos: List[str], setup_script: str, number: int,
                        *args) -> None:
        """Times algorithms performance using timeit.

        CAUTION: Executes code directly.

        Parameters
        ----------
        algos
            List of full namespace function names.

        setup_script
            Import statements to allow timeit access to the functions.

        number
            Number of times to run the funciton

        *args
            Parameters to the function.
            
        """
        for algo_name in algos:
            print('\nRAN {} {} times with args {}'.format(algo_name, number,
                                                          *args))
            print(timeit('{}({})'.format(algo_name, *args),
                         setup=setup_script, number=number))
