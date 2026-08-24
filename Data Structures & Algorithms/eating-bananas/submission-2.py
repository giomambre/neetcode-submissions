class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        n = len(piles)
        R = max(piles)
        res = R
        L = 1

        while L <= R :
            middle = (L+ R ) // 2
            total = 0
            for n in piles:
                
                total += math.ceil(n/middle)

            if total <= h: 
                res = min(res,middle)
                R = middle-1
            else:
                L = middle + 1

        return res