# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def checksubtree(node1, node2):
            if not node1 and not node2:
                return True
            elif not node1 or not node2:
                return False
            elif node1.val == node2.val:
                return checksubtree(node1.left, node2.left) and checksubtree(node1.right, node2.right)
            else:
                return False
            
        def traverse(node, res):
            if not node:
                return False
            elif node.val == subRoot.val:
                if res or checksubtree(node, subRoot):
                    res = True
                    return res
            return traverse(node.left, res) or traverse(node.right, res)

        return traverse(root, False)
