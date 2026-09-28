class Solution:
    def trap(self, height: List[int]) -> int:
        N = len(height)
        left_max , right_max = [0]*N, [0]*N

        res = 0

        for i in range(N):
            left_max[i] = height[i] if i == 0 else max(height[i],left_max[i-1])
        
        for i in range(N-1,-1,-1):
           right_max[i] = height[i] if i == N-1 else max(height[i],right_max[i+1])
        

        for i in range(N):

            res +=  min(right_max[i], left_max[i]) - height[i]
        
        return res

         