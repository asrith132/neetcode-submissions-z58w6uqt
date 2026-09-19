# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            if not node:
                return (0, True)
            
            l, lvalid = dfs(node.left)
            r, rvalid = dfs(node.right)

            if lvalid and rvalid and abs(l - r) <= 1:
                return (max(l, r) + 1, True)
            else:
                return (max(l, r) + 1, False)
        _, res = dfs(root)
        return res
