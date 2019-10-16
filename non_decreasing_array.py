"""Non Decreasing Array."""


from typing import List


class NonDecreasingArray:
    """Given an array with n integers, check if it could become a
    non-decreasing array by modifying at most 1 element to any number.

    Non-decreasing array is defined as array[i] <= array[i+1] for all i.

    https://leetcode.com/problems/non-decreasing-array/

    Notes
    -----
    is_non_decr_array(): faster >22%, mem < 11%

    is_non_decr_array_2(): faster >49%, mem < 79% even though this algorithm
    calls is_non_decr_array, it only does so for the cases where it is not
    trivial to determine whether solution exists or not. Thereby reducing much
    computations.
    """
    @staticmethod
    def is_non_decr_array(nums: List[int]) -> bool:
        """When encountering a decreasing integer, there are 2 cases of
        problems in this monotonically increasing array.
        - Case 1: The preceeding integer is the cause of the error, ie,
        [1, 2, 100, 3]
        - Case 2: The decreased integer is the cause of the error. ie,
        [1, 2, 1, 3]

        Since we are allowed only 1 edit, if even after we remove either
        problem integer and array is still not fixed, it's not possible to
        fix with only editing 1 element.

        Parameters
        ----------
        nums
            Array to check.

        Returns
        -------
        Can 1 element change make it a non-decreasing array.

        Examples
        --------
        >>> NonDecreasingArray.is_non_decr_array([4, 2, 3])
        True
        >>> NonDecreasingArray.is_non_decr_array([4, 2, 1])
        False
        """
        if len(nums) <= 2:
            return True

        prev_number = float('-inf')
        for idx, num in enumerate(nums):
            # Problem area
            if num < prev_number:
                # remove last number and see if it's fixed
                nums_copy = nums.copy()
                nums_copy.pop(idx-1)
                is_fixed = all([x <= y for x, y in zip(nums_copy,
                                                       nums_copy[1:])])
                if is_fixed:
                    return True
                else:
                    # remove this number and see if it's fixed
                    nums_copy.insert(idx-1, nums[idx-1])
                    nums_copy.pop(idx)
                    is_fixed = all([x <= y for x, y in zip(nums_copy,
                                                           nums_copy[1:])])
                    if is_fixed:
                        return True
                    else:
                        return False
            prev_number = num
        return True

    @staticmethod
    def is_non_decr_array_2(nums: List[int]) -> bool:
        """Break problem into 2 trivial and 1 core case.

        - Case 1: if array in order no issue.
        - Case 2: if 2 decreasing elements, unfixable.
        - Case 3: if 1 decreasing element, analyze much smaller problem
        locally.
        """
        if len(nums) <= 2:
            return True

        decr_ints = [1 if x > y else 0 for x, y in zip(nums, nums[1:])]
        if sum(decr_ints) == 0:
            return True
        elif sum(decr_ints) >= 2:
            return False
        else:
            problem_start = decr_ints.index(1)-1
            problem_end = min(problem_start+4, len(nums))
            return NonDecreasingArray.is_non_decr_array(nums[problem_start:problem_end])


if __name__ == '__main__':
    from algorithms.performance import PerfBenchmark

    algos = ['NonDecreasingArray.is_non_decr_array',
             'NonDecreasingArray.is_non_decr_array_2']
    setup_script = 'from algorithms.non_decreasing_array import NonDecreasingArray'
    test_input1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 2]
    test_input2 = [1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 2]

    PerfBenchmark.benchmark_algos(algos, setup_script, 100, test_input1)
    PerfBenchmark.benchmark_algos(algos, setup_script, 100, test_input2)

