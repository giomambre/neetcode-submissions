class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        res = 0
        intervals.sort(key = lambda x: x[0])
        curr_end = intervals[0][1]


        for s,e in intervals[1:]:

            if s < curr_end:
                res +=1
                curr_end = min(curr_end,e)
            else:
                curr_end = e
        
        return res
         

