class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)
        res = 0
        if n <= 1:
            return 0
        L = 0
        # [1,1,2,2,3,3]
        for R in range(1,n):
            
            if prices[R] < prices[L]:
                L = R
            else:
                profit = prices[R] - prices[L]
                res = max(res, profit)
            
        return res
            
            
        

 # 1 
        

                
            

        