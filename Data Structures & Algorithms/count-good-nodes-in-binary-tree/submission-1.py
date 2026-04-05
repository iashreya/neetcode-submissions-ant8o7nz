# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.good_nodes = 0

        def dfs(node, path=[]):
            if node is None:
                return
            
            is_good = True
            print(node.val, path)
            for i in path:
                if i > node.val:
                    is_good = False

            if is_good:
                self.good_nodes += 1
            
            path.append(node.val)
            dfs(node.right, path[:])
            dfs(node.left, path[:])

        dfs(root)
        return self.good_nodes