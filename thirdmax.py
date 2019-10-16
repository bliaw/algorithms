"""Find the third max of array."""


from typing import List


class ThirdMax:
    """Given a non-empty array of integers, return the third maximum number
    in the array.  If it does not exist, return the max of the list.

    Must be O(n)

    https://leetcode.com/problems/third-maximum-number/

    Notes
    -----
    thirdmax: faster > 67%, mem < 15%
    thirdmax_2: faster > 65%, mem < 27%.  Memory can be made to be O(1).

    """

    @staticmethod
    def thirdmax(nums: List[int]) -> int:
        """Pop off max of unique values 3 times.

        Parameters
        ----------
        nums
            List of ints.

        Returns
        -------
        Third max or if does not exist, the max.

        Examples
        --------
        >>> ThirdMax.thirdmax([3, 2, 1])
        1
        >>> ThirdMax.thirdmax([1, 2])
        2
        >>> ThirdMax.thirdmax([2, 2, 3, 1])
        1

        """
        # Reduce problem to distinct list of ints.
        nums_unique = list(set(nums))
        # Case 1 - if less than 3 distinct value.
        # Case 2 - pop off max of list 3 times.
        if len(nums_unique) <= 2:
            return max(nums_unique)
        else:
            thirdmax = None
            for _ in range(3):
                thirdmax = nums_unique.pop(nums_unique.index(max(nums_unique)))
            return thirdmax

    @staticmethod
    def thirdmax_2(nums: List[int]) -> int:
        """Comb method by keeping track of top 3 maxes."""
        top_maxes = [float('-inf'), float('-inf'), float('-inf')]
        nums_unique = set(nums)

        if len(nums_unique) <= 2:
            return max(nums_unique)
        else:
            for num in nums_unique:
                if num < top_maxes[0]:
                    continue
                elif num > top_maxes[2]:
                    top_maxes = [top_maxes[1], top_maxes[2], num]
                elif num > top_maxes[1]:
                    top_maxes = [top_maxes[1], num, top_maxes[2]]
                elif num > top_maxes[0]:
                    top_maxes = [num, top_maxes[1], top_maxes[2]]
            return int(top_maxes[0])
