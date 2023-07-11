"""
LeetCode
863. All Nodes Distance K in Binary Tree
July 2023 Challenge
jramaswami
"""


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:

        # Convert tree into a undirected graph
        graph = collections.defaultdict(list)
        target_node = None
        def rec(parent, node):
            if node is None:
                return

            if parent:
                graph[parent.val].append(node.val)
                graph[node.val].append(parent.val)
            
            rec(node, node.left)
            rec(node, node.right)

        rec(None, root)

        # Use BFS to find all the nodes at the right distance
        queue = collections.deque()
        visited = set()
        queue.append((0, target.val))
        visited.add(target.val)
        soln = []
        while queue:
            distance, node = queue.popleft()
            if distance == k:
                soln.append(node)
            else:
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((distance + 1, neighbor))
        return soln
