# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        queue = deque([root])

        if not root:
            return []

        res = []

        while queue :
            tmp = []
            for i in range(len(queue)):
                curr_node = queue.popleft()
                L  = curr_node.left
                if L:
                    queue.append(L)
                R = curr_node.right
                if R:
                    queue.append(R)
                tmp.append(curr_node.val)
            res.append(tmp)
        
        return res
            
            