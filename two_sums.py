"""Two Sums."""

import collections
from typing import List

from datastructures.trees import BinarySearchTree
from datastructures.nodes import BinaryTreeNode


###############################################################
##                       Two Sums                            ##
###############################################################
# @profile
def two_sums(nums: List[int], target: int) -> List[int]:
    """Two Sums.

    https://leetcode.com/problems/two-sum/

    Given array of integers, return indices of the 2 numbers such that they
    add up to a specific target.

    Assume for a given array, there is exactly 1 solution.

    Notes
    -----
    two_sums: faster > 92%, mem < 15%
    two_sums_2: faster > 28%, mem < 86%
    two_sums_3: time limit exceeded
    Winner - two_sums_2 - easy to understand and low mem usage.

    Parameters
    ----------
    nums:
        Array of integers.
    target:
        Desired target.

    Returns
    -------
    list
        List of indices of the 2 numbers that add up to the target

    Example
    -------
    >>> nums = [2, 7, 11, 9]
    >>> target = 9
    >>> two_sums(nums, target)
    [0, 1]

    """
    # Go thru list once, check to see if any previous number looking for it.
    num_wanted = dict()
    for idx, num in enumerate(nums):
        complement = target - num
        # Check if anyone is looking for this number.
        # If not, log the complement number this numbers is looking for.
        try:
            return [num_wanted[num], idx]
        except KeyError:
            num_wanted[complement] = idx


# @profile
def two_sums_2(nums: List[int], target: int) -> List[int]:
    """Go thru list once and look to see if complement is in list."""
    for idx, num in enumerate(nums):
        complement = target - num
        nums_copy = nums.copy()
        nums_copy[idx] = None
        if complement in nums_copy:
            return [idx, nums_copy.index(complement)]


# @profile
def two_sums_3(nums: List[int], target: int) -> List[int]:
    """Brute force pass thru twice."""
    for first_idx in range(len(nums)):
        for second_idx in range(len(nums)):
            if first_idx == second_idx:
                continue
            if nums[first_idx] + nums[second_idx] == target:
                return [first_idx, second_idx]


###############################################################
##                       Two Sums II                         ##
###############################################################
def two_sums_II(numbers: List[int], target: int) -> List[int]:
    """Two Sums II

    https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

    Given an array of integers already sorted in ascending order, find 2
    numbers such that it adds up to the target number. Return the index of
    the 2 numbers.

    index1 must be less than index2.

    Indices are 1-based instead of 0 based.

    Exactly 1 solution and may not use element more than once.

    Notes
    -----
    two_sums_II: faster > 94%, mem < 10%
    two_sums_II_2: faster > 81%, mem <43%
    two_sums_II_3: faster > 81%, mem <85%
    Winner - two_sums_II_2 is most straight forward.

    Parameters
    ----------
    nums:
        Array of integers.
    target:
        Desired target.

    Returns
    -------
    list
        List of indices of the 2 numbers that add up to the target

    Example
    -------
    >>> nums = [2, 7, 11, 15]
    >>> target = 9
    >>> two_sums_II(nums, target)
    [1, 2]
    """
    # Case 1 - the 2 numbers are the same.
    # Because sorted and unique solution and the answer can occur at most
    # twice (even though non answers can occur some arbitrarily large amount
    # of times. We thus check this special case where target / 2 which results
    # in the 2 numbers being the same, and therefore next to each other.
    counts = collections.Counter(numbers)
    if target % 2 == 0 and counts[int(target/2)] == 2:
        return [numbers.index(int(target/2)) + 1, numbers.index(int(target/2)) + 2]

    # Case 2 - the 2 numbers are different.
    # Compress numbers to unique OrderedDict - which preserves order to find
    # the 2 numbers we want. Once we've found the numbers we want we can
    # lookup index in the original array.
    numbs_unique = list(collections.OrderedDict.fromkeys(numbers))

    for first_num_unique_idx, first_num in enumerate(numbs_unique):
        complement = target - first_num
        # Since array is sorted, just look in the slice of the array from
        # this point on.
        if complement in numbs_unique[first_num_unique_idx+1:]:
            return [numbers.index(first_num) + 1, numbers.index(complement) + 1]


def two_sums_II_2(numbers: List[int], target: int) -> List[int]:
    # Go thru list once, check to see if any previous number looking for it.
    num_wanted = dict()
    for idx, num in enumerate(numbers):
        complement = target - num
        # Check if anyone is looking for this number.
        # If not, log the complement number this numbers is looking for.
        try:
            return [num_wanted[num] + 1, idx + 1]
        except KeyError:
            num_wanted[complement] = idx


def two_sums_II_3(numbers: List[int], target: int) -> List[int]:
    # Use left and right pointers and increment to hones in to target.
    assert len(numbers) >= 2

    left = 0
    right = len(numbers) - 1

    while left != right:
        total = numbers[left] + numbers[right]
        if  total > target:
            right -= 1
        elif total < target:
            left += 1
        elif total == target:
            return [left + 1, right + 1]
        else:
            break


def two_sums_IV(root: BinaryTreeNode, k: int) -> bool:
    """Given a binary search tree of nodes values x (which are unique) and
    target y, return bool value of 'there  exists 2 elements x1, x2 in BST that
    sum to target y'.

    Parameters
    ----------
    root : BinaryTreeNode
        Root node of the BST.
    k : int
        Target number to sum to.

    Returns
    -------
    bool
        True if there is a solution.

    Notes
    -----
    two_sums_IV: faster > 13%, mem <5%
    two_sums_IV_2: faster > 86%, mem < 87%

    Examples
    --------
    >>> tree = BinarySearchTree(collections.OrderedDict([(5, 5), (3, 3), \
    (6, 6), (2, 2), (4, 4), (7, 7)]))
    >>> two_sums_IV(tree._root, 9)
    True
    >>> two_sums_IV(tree._root, 28)
    False
    >>> tree = BinarySearchTree(collections.OrderedDict([(1, 1)]))
    >>> two_sums_IV(tree._root, 2)
    False

    """
    # Approach 1 - collapse tree into sorted array and solve it as array problem
    BST_to_list = []
    frontier = collections.deque([])
    frontier.append(root)
    while frontier:
        node = frontier.popleft()
        BST_to_list.append(node.item)
        if node.left_child is not None:
            frontier.append(node.left_child)
        if node.right_child is not None:
            frontier.append(node.right_child)

    BST_to_list.sort()

    if two_sums_II(BST_to_list, k) is not None:
        return True
    return False


def two_sums_IV_2(root: BinaryTreeNode, k: int) -> bool:
    # Approach 2 - iter thru tree in breadth first fashion and see if any of
    # values we're looking for we've already come across. Note this does not
    # use the knowledge of BST structure at all.
    prev_node_vals = []
    frontier = collections.deque([])
    frontier.append(root)
    while frontier:
        node = frontier.popleft()
        complement = k - node.item
        if complement in prev_node_vals:
            return True

        if node.left_child is not None:
            frontier.append(node.left_child)
        if node.right_child is not None:
            frontier.append(node.right_child)
        prev_node_vals.append(node.item)
    return False


if __name__ == '__main__':
    current_problem = 'Two Sums IV'
    import timeit

    if current_problem == 'Two Sums':
        nums = [2, 7, 11, 9, 1, 8, 12, 939, 29, 492, 38, 39, 44, 79, 24]
        target = 83

        print(timeit.timeit('two_sums(nums, target)',
                            setup='from __main__ import two_sums, nums, target',
                            number=10000))

        print(timeit.timeit('two_sums_2(nums, target)',
                            setup='from __main__ import two_sums_2, nums, target',
                            number=10000))

        print(timeit.timeit('two_sums_3(nums, target)',
                            setup='from __main__ import two_sums_3, nums, target',
                            number=10000))
    elif current_problem == 'Two Sums II':
        nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2]
        target = 3

        nums2 = [0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 5]
        target2 = 6

        import timeit
        print(timeit.timeit('two_sums_II(nums, target)',
                            setup='from __main__ import two_sums_II, nums, target',
                            number=10000))
        print(timeit.timeit('two_sums_II(nums2, target2)',
                            setup='from __main__ import two_sums_II, nums2, target2',
                            number=10000))

        print(timeit.timeit('two_sums_II_2(nums, target)',
                            setup='from __main__ import two_sums_II_2, nums, target',
                            number=10000))
        print(timeit.timeit('two_sums_II_2(nums2, target2)',
                            setup='from __main__ import two_sums_II_2, nums2, target2',
                            number=10000))

        print(timeit.timeit('two_sums_II_3(nums, target)',
                            setup='from __main__ import two_sums_II_3, nums, target',
                            number=10000))
        print(timeit.timeit('two_sums_II_3(nums2, target2)',
                            setup='from __main__ import two_sums_II_3, nums2, target2',
                            number=10000))
    elif current_problem == 'Two Sums IV':
        tree = BinarySearchTree(collections.OrderedDict([(5, 5), (3, 3), (6, 6),
                                                         (2, 2), (4, 4), (7, 7)]))
        target = 9
        target2 = 28
        tree2 = BinarySearchTree(collections.OrderedDict([(5, 5), (3, 3), (6, 6),
                                                         (4, 4), (7, 7)]))

        print(timeit.timeit('two_sums_IV(tree._root, target)',
                            setup='from __main__ import two_sums_IV, tree, target',
                            number=10000))
        print(timeit.timeit('two_sums_IV(tree._root, target2)',
                            setup='from __main__ import two_sums_IV, tree, target2',
                            number=10000))
        print(timeit.timeit('two_sums_IV(tree2._root, target2)',
                            setup='from __main__ import two_sums_IV, tree2, target2',
                            number=10000))

        print(timeit.timeit('two_sums_IV_2(tree._root, target)',
                            setup='from __main__ import two_sums_IV_2, tree, target',
                            number=10000))
        print(timeit.timeit('two_sums_IV_2(tree._root, target2)',
                            setup='from __main__ import two_sums_IV_2, tree, target2',
                            number=10000))
        print(timeit.timeit('two_sums_IV_2(tree2._root, target2)',
                            setup='from __main__ import two_sums_IV_2, tree2, target2',
                            number=10000))







