class Solution:
    def maxArea(self, heights: List[int]) -> int:
        R = len(heights)- 1
        L = 0
        res = 0

        while L < R:

            water_lv = min(heights[R],heights[L]) * (R-L)

            res = max(res,water_lv)
            #print(water_lv)
            if heights[R] >= heights[L]:
                
                L+=1
            else :
                R-=1
        
        return res

        