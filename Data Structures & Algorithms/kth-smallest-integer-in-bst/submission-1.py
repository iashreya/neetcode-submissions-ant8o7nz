# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        self.answer = -1
        def inorder(root):
            if root is None:
                return
            
            # Inorder traversal where we keep count of
            # the number of elements already seen
            inorder(root.left)
            self.count += 1
            if self.count == k:
                self.answer = root.val
                return
            inorder(root.right)
        
        inorder(root)
        return self.answer