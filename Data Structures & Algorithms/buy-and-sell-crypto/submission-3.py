class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        res = 0
        cur = prices[0]


        for i in range(len(prices)-1):
            if prices[i] < cur:
                cur = prices[i]
        
            if prices[i+1] >= cur:
                res = max(res,prices[i+1] - cur)
            
        return res
        