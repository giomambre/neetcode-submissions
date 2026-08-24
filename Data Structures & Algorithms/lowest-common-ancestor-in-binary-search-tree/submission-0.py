# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        while root:
            curr_val = root.val
            if p.val > curr_val and q.val > curr_val:
                root = root.right
            elif p.val < curr_val and q.val < curr_val:
                root = root.left
            
            else:
                return root
        