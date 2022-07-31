"""
LeetCode :: July 2022 Challenge :: Range Sum Query - Mutable
jramaswami
"""


from sympy import arg


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
        self.st = [0] * (len(nums) * 4)
        self.nums = nums
        self._build(1, 0, len(self.nums) - 1)

    def _build(self, tree_node, seg_left, seg_right):
        if seg_left == seg_right:
            self.st[tree_node] = self.nums[seg_left]
        else:
            seg_mid = seg_left + ((seg_right - seg_left) // 2)
            left_child = tree_node * 2
            right_child = left_child + 1
            self._build(left_child, seg_left, seg_mid)
            self._build(right_child, seg_mid + 1, seg_right)
            self.st[tree_node] = self.st[left_child] + self.st[right_child]

    def _update(self, tree_node, seg_left, seg_right, index, val):
        if seg_left == seg_right:
            self.st[tree_node] = val
        else:
            seg_mid = seg_left + ((seg_right - seg_left) // 2)
            left_child = tree_node * 2
            right_child = left_child + 1
            if index <= seg_mid:
                self._update(left_child, seg_left, seg_mid, index, val)
            else:
                self._update(right_child, seg_mid + 1, seg_right, index, val)
            self.st[tree_node] = self.st[left_child] + self.st[right_child]

    def update(self, index, val):
        """Updates the value of nums[index] to be val."""
        self._update(1, 0, len(self.nums) - 1, index, val)

    def _query(self, tree_node, seg_left, seg_right, qry_left, qry_right):
        if qry_left <= seg_left and seg_right <= qry_right:
            return self.st[tree_node]
        if qry_right < seg_left:
            return 0
        if seg_right < qry_right:
            return 0
        seg_mid = seg_left + ((seg_right - seg_left) // 2)
        left_child = tree_node * 2
        right_child = left_child + 1
        return (
            self._query(left_child, seg_left, seg_mid, qry_left, qry_right) +
            self._query(right_child, seg_mid + 1, seg_right, qry_left, qry_right)
        )

    def sumRange(self, left, right):
        """
        Returns the sum of the elements of nums between indices left and right.
        """
        return self._query(1, 0, len(self.nums) - 1, left, right)


#
# Testing
#


null = None


def test_1():
    A = NumArray([1, 3, 5])
    assert A.sumRange(0, 2) == 9
    A.update(1, 2)
    assert A.sumRange(0, 2) == 8


def test_2():
    "WA"
    methods = ["NumArray","sumRange","sumRange","sumRange","update","update","update","sumRange","update","sumRange","update"]
    arguments = [[[0,9,5,7,3]],[4,4],[2,4],[3,3],[4,5],[1,7],[0,8],[1,2],[1,9],[4,4],[3,4]]
    expected = [null,3,15,7,null,null,null,12,null,5,null]
    na = NumArray(*arguments[0])
    for m, a, e in zip(methods[1:], arguments[1:], expected[1:]):
        assert getattr(na, m)(*a) == e