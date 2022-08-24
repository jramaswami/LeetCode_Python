"""
LeetCode :: 297. Serialize and Deserialize Binary Tree
jramaswami
"""

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        NULL = "1111111111"
        H = [NULL]
        def traverse(node, i):
            if node is None:
                return

            while len(H) <= i:
                H.append(NULL)

            H[i] = f"{node.val:010b}")
            traverse(node.left, i*2)
            traverse(node.right, (i*2)+1)

        traverse(root, 1)
        return "".join(H)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        NULL = "1111111111"
        if data == [NULL]:
            return None
        def traverse(i):
            if i >= len(H):
                return None
            if data[i*10:(i+1)*10] == NULL:
                return None
            left_child = traverse(i * 2)
            right_child = traverse((i * 2) + 1)
            return TreeNode(int(data[i*10:(i+1)*10], 2), left_child, right_child)

        return traverse(1)