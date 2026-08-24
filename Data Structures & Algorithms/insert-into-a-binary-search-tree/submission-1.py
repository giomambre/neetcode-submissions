# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        def dfs(curr):

            if curr is None:
                curr = TreeNode(val)
            elif curr.val > val:
                curr.left = dfs(curr.left)
            else:
                curr.right = dfs(curr.right)
            
            return curr
        
        root = dfs(root)
        return root
        