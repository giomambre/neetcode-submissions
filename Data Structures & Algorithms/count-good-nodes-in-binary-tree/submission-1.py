# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        if not root:
            return None

        def dfs(node,cur_max):
            nonlocal res
            if not node:
                return
            
            if node.val >= cur_max:
                res +=1
            
            cur_max = max(node.val,cur_max)
            dfs(node.left,cur_max)
            dfs(node.right,cur_max)
        dfs(root,float("-inf"))
        return res
        
        