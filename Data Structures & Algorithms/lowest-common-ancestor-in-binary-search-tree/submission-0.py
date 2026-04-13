# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        res = root
        stack = []
        stack.append(root)
        less = more = 0
        if p.val < q.val:
            less = p
            more = q
        else:
            less = q
            more = p
        while stack:
            node = stack.pop()
            if less.val <= node.val and more.val >= node.val:
                return node
            if node.left is not None:
                stack.append(node.left)
            if node.right is not None:
                stack.append(node.right)
        return res