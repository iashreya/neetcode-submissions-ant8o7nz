# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        level_nodes = []
        def dfs(root, level):
            if root is None:
                return
            
            if level == len(level_nodes):
                level_nodes.append([])

            level_nodes[level].append(root.val)
            dfs(root.left, level+1)
            dfs(root.right, level+1)

        dfs(root, 0)
        answer = [i[-1] for i in level_nodes]
        return answer
