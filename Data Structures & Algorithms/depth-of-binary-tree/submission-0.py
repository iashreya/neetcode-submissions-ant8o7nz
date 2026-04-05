# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findDepth(self, root, depth=0):
        if root == None:
            return depth

        return max(self.findDepth(root.left, depth+1),
                    self.findDepth(root.right, depth+1))

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0
        return self.findDepth(root, depth)