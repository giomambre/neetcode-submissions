class Solution:
    def dailyTemperatures(self, tmps: List[int]) -> List[int]:
        N = len(tmps)
        res = [0] * N
        stack = []
        for i,t in enumerate(tmps):

            while len(stack) >= 1 and stack[-1][0] < t:
                cur_t , j = stack.pop()
                res[j] = i - j
            
            stack.append((t,i))
        
        [381,363,354]
        return res