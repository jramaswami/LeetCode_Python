"""
LeetCode
1028. Recover a Tree From Preorder Traversal
February 2025 Challenge
jramaswami
"""


import collections
import dataclasses


@dataclasses.dataclass(frozen = True)
class NodeSpec:
    """ Model the specification for a Node
    """
    level: int
    value: int


def parse_traversal_string(traversal):
    """Parse traversal string into deque of NodeSpecs
    """
    IN_LEVEL = 0
    IN_DIGITS = 1
    result = collections.deque()
    state = IN_LEVEL
    curr_level = 0
    curr_value = 0
    for char in traversal:
        if char.isdigit():
            if state == IN_DIGITS:
                curr_value = (10 * curr_value) + int(char)
            else:
                curr_value = int(char)
                state = IN_DIGITS
        else:
            if state == IN_DIGITS:
                result.append(NodeSpec(curr_level, curr_value))
                curr_level = curr_value = 0
                state = IN_LEVEL
            curr_level += 1
    result.append(NodeSpec(curr_level, curr_value))
    return result


def rec(curr_level, traversal_queue):
    """Return subtree given current level and traversal queue
    """
    curr_node = None
    if traversal_queue and curr_level == traversal_queue[0].level:
        node_spec = traversal_queue.popleft()
        curr_node = TreeNode(node_spec.value)
        curr_node.left = rec(curr_level + 1, traversal_queue)
        curr_node.right = rec(curr_level + 1, traversal_queue)
    return curr_node


class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        # Parse the traversal string
        traversal_queue = parse_traversal_string(traversal)
        return rec(0, traversal_queue)
