"""
LeetCode :: June 2021 Challenge :: Range Sum Query - Mutable
jramaswami
"""


class NumArray:
    """
    Given an integer array nums, handle multiple queries of the following
    types:

    1. Update the value of an element in nums.
    2. Calculate the sum of the elements of nums between indices left and right
       inclusive where left <= right.

    The solution is to use a segment tree.
    Query and update operations are O(log n).
    """

    def __init__(self, nums):
        """Initializes the object with the integer array nums."""
        self.nums = nums
        self.tree = [0] * (4 * len(nums))
        self._build(1, 0, len(nums)-1)


    def _build(self, node, start_index, end_index):
        """Recursive function to build segement tree."""
        if start_index == end_index:
            self.tree[node] = self.nums[start_index]
            return

        mid_index = (start_index + end_index) // 2
        left_child = 2 * node
        right_child = left_child + 1

        self._build(left_child, start_index, mid_index)
        self._build(right_child, mid_index + 1, end_index)

        self.tree[node] = self.tree[left_child] + self.tree[right_child]

    def _update(self, node, start_index, end_index, upd_index, upd_value):
        """Recursive function to update segment tree."""
        if start_index == end_index:
            self.tree[node] = upd_value
            self.nums[upd_index] = upd_value
            return

        mid_index = (start_index + end_index) // 2
        left_child = 2 * node
        right_child = left_child + 1

        if upd_index <= mid_index:
            self._update(left_child, start_index, mid_index, upd_index, upd_value)
        else:
            self._update(right_child, mid_index + 1, end_index, upd_index, upd_value)

        self.tree[node] = self.tree[left_child] + self.tree[right_child]

    def _query(self, node, start_index, end_index, query_left, query_right):
        """Recursive function to query segment tree."""
        if (query_left <= start_index and end_index <= query_right):
            return self.tree[node]

        if (start_index > query_right or end_index < query_left):
            return 0

        mid_index = (start_index + end_index) // 2
        left_child = 2 * node
        right_child = left_child + 1

        left_sum = self._query(left_child, start_index, mid_index, query_left, query_right)
        right_sum = self._query(right_child, mid_index + 1, end_index, query_left, query_right)
        return left_sum + right_sum

    def update(self, index, val):
        """Updates the value of nums[index] to be val."""
        self._update(1, 0, len(self.nums) - 1, index, val)

    def sumRange(self, left, right):
        """
        Returns the sum of the elements of nums between indices left and right.
        """
        return self._query(1, 0, len(self.nums) - 1, left, right)


def test_1():
    A = NumArray([1, 3, 5])
    assert A.sumRange(0, 2) == 9
    A.update(1, 2)
    assert A.sumRange(0, 2) == 8
