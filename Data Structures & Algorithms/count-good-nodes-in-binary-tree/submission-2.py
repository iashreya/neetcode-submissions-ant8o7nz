# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.good_nodes = 0

        def dfs(node, max_yet):
            if node is None:
                return

            self.good_nodes = self.good_nodes+1 if node.val >= max_yet else self.good_nodes
            max_yet = max(max_yet, node.val)
            dfs(node.right, max_yet)
            dfs(node.left, max_yet)

        dfs(root, float('-inf'))
        return self.good_nodes