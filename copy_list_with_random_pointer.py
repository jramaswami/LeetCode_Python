"""
LeetCode :: March 2022 Challenge :: 138. Copy List with Random Pointer
jramaswmai
"""


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return None

        nodes = []
        curr = head
        while curr:
            # Append node into nodes.
            nodes.append(curr)
            # Append a copy
            nodes.append(Node(curr.val))
            curr = curr.next

        # Set all nodes/copies next so that they are in a linked
        # list where all even indexes are nodes and odd indexes
        # are copies.
        for left, right in zip(nodes[:-1], nodes[1:]):
            left.next = right

        # Set the random nodes by following the link from the original.
        # The original random will point to the copy random.  Use that
        # to set the copy node's random.
        for i in range(0, len(nodes), 2):
            new_random = None
            if nodes[i].random:
                new_random = nodes[i].random.next
            if i + 1 < len(nodes):
                nodes[i+1].random = new_random

        # Fix all the next pointers to separate the two lists.
        for i in range(0, len(nodes)):
            if i + 2 < len(nodes):
                nodes[i].next = nodes[i+2]

        return nodes[1]
