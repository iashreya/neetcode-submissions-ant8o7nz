# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        ancestors = [] 
        def findAncestors(root, node):
            if root == None:
                return False
            if root.val == node.val:
                ancestors.append(root)
                return True

            left = findAncestors(root.left, node)
            right = findAncestors(root.right, node)

            if left or right:
                ancestors.append(root)
                return True

            return False

        findAncestors(root, p)
        ancestors.reverse()
        p_ancestors = ancestors
        ancestors = []
        findAncestors(root, q)
        ancestors.reverse()
        q_ancestors = ancestors 

        lca = root
        for i in range(min(len(p_ancestors), len(q_ancestors))):
            if p_ancestors[i] == q_ancestors[i]:
                lca = p_ancestors[i]
            else:
                break

        return lca


            



            
