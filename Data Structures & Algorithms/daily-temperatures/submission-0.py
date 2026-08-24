class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    # stack = [(40,5),(28,6)]
    # current = 
    #res = [1,4,1,2,1,0,0]
        n = len(temperatures)
        stack = []
        res = [0]*n

        for i in range(n):
            if not stack:
                stack.append((temperatures[i],i)) # can optimize space
            else:
                while stack and temperatures[i] > stack[-1][0] :
                    val , j = stack.pop()
                    res[j] = i - j
                
                stack.append((temperatures[i],i))
        return res

        