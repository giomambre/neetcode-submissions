class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key = lambda a:a[0])
        res = [intervals[0]]
        for i in range(1,len(intervals)):
            
            last = res[-1]

            if last[1] >= intervals[i][0]:

                res[-1][1] = max(last[1],intervals[i][1])

            else:
                res.append(intervals[i])

        return res 



           

