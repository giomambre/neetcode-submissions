class Solution:
    def rob(self, nums: List[int]) -> int:
    #dp = [12,16] cur + dp[0] <= dp[1]
    # [1,100,3,3]
    # dp[100,100] # 3 
        if not nums:
            return 0

        n = len(nums)
        if n <=1:
            return nums[0]
        if n <=2:
            return max(nums[0],nums[1])

        dp = [nums[0], max(nums[0], nums[1])]
        for i in range(2,n):
            tmp = dp[1]
            if dp[0] + nums[i] > dp[1]:
                tmp = dp[0] + nums[i]

            else:
                tmp = dp[1]
            
            dp[0] , dp[1] = dp[1] , tmp
        
        return dp[1]         
            