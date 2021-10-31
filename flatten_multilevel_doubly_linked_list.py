"""
LeetCode :: October 2021 Challenge :: 430. Flatten a Multilevel Doubly Linked List
jramaswami
"""

class Solution:
    def flatten(self, head):

        def gather(node, acc):
            """Recursive function to gather all node values."""
            if node is None:
                return

            acc.append(node.val)
            gather(node.child, acc)
            gather(node.next, acc)

        def build(prev_node, index, acc):
            """Recursive function to build flat list."""
            if index >= len(acc):
                return
            new_node = Node(acc[index], prev_node, None, None)
            prev_node.next = new_node
            build(new_node, index + 1, acc)

        # Gather all node values.
        acc = []
        gather(head, acc)

        # Build a new list with the values
        if acc:
            new_head = Node(acc[0], None, None, None)
            build(new_head, 1, acc)
            return new_head
