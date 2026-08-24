class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [cost[0],cost[1]]

        for i in range(2,len(cost)):

            res = min(dp[0],dp[1])
            dp[0] , dp[1] = dp[1] , cost[i] + min(dp[0], dp[1])
        
        return min(dp[0],dp[1])