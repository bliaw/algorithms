"""Rotate array by some number k."""


from typing import List


class RotateArray:
    """Given an array, rotate the array in place to the right by k steps.

    k is non-negative.

    Space complexity requirement of O(1)

    https://leetcode.com/problems/rotate-array/

    Notes
    -----
    rotate: faster >80%, mem < 24%
    """

    @staticmethod
    def rotate(nums: List[int], k: int) -> List[int]:
        """Outer loop - start with offset 0 -> k. Inner loop - rotate single
        elements that are k steps apart.

        Parameters
        ----------
        nums
            Array of integers.
        k
            Number of steps to rotate.

        Returns
        -------
        None since do it in place.

        Examples
        --------
        >>> nums = [1, 2, 3, 4, 5, 6, 7]
        >>> RotateArray.rotate(nums, 3)
        >>> nums
        [5, 6, 7, 1, 2, 3, 4]
        >>> nums = [-1, -100, 3, 99]
        >>> RotateArray.rotate(nums, 2)
        >>> nums
        [3, 99, -1, -100]

        """
        m = len(nums)
        if m > 1:
            # Only manipulate if modded_k !=0
            modded_k = k % m
            if modded_k != 0:
                # Initialize buffer
                pop_idx = 0
                buffer_await_insert = nums[pop_idx]
                nums[pop_idx] = None

                # Outer loop - set offset starting point.
                for _ in range(modded_k):
                    if buffer_await_insert is None:
                        pop_idx += 1
                        buffer_await_insert = nums[pop_idx]
                        nums[pop_idx] = None
                    # Inner loop - step thru array in k increments.
                    for idx in range(pop_idx, m, modded_k):
                        insert_idx = (idx + modded_k) % m
                        pop_idx = insert_idx
                        buffer_popped = nums[insert_idx]
                        nums[insert_idx] = buffer_await_insert
                        buffer_await_insert = buffer_popped


