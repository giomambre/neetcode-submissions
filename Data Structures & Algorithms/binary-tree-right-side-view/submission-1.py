# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        def bfs():

            queue = deque([root])

            while queue:

                for i in range(len(queue)):
                    curr_node = queue.popleft()
                    L  = curr_node.left
                    if L:
                        queue.append(L)
                    R = curr_node.right
                    if R:
                        queue.append(R)
                res.append(curr_node.val)
        

        bfs()
        return res

