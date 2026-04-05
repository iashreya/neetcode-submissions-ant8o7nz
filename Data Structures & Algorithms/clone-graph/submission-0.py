"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None

        old_new_map = {} # old_node : new_node

        def dfs(node):
            if node in old_new_map:
                return old_new_map[node]
            
            copy = Node(node.val)
            old_new_map[node] = copy

            for i in node.neighbors:
                copy.neighbors.append(dfs(i))

            return copy

        return dfs(node)

