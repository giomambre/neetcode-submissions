class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x: x[0])
        
        res = [intervals[0]]

        for interval in intervals[1:]:
            # Se l'intervallo corrente si sovrappone con l'ultimo salvato
            if interval[0] <= res[-1][1]:
                res[-1][1] = max(res[-1][1], interval[1])
            else:
                res.append(interval)
                
        return res