"""
Functions for testing linked list problems on LeetCode.
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return f"ListNode(val={self.val}, next={self.next})"


def make_list(arr):
    if arr == []:
        return None
    head = ListNode(arr[0])
    node = head
    for x in arr[1:]:
        new_node = ListNode(x)
        node.next = new_node
        node = new_node
    return head


def make_arr(node):
    arr = []
    while node:
        arr.append(node.val)
        node = node.next
    return arr


def reverse_linked_list(node):
    """Reverse the linked list in place."""
    previous = None
    current = node
    following = node

    while current:
        following = following.next
        current.next = previous
        previous = current
        current = following

    return previous



