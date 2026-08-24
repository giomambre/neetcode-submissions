class Solution:
    def dailyTemperatures(self, tmps: List[int]) -> List[int]:
        N = len(tmps)
        res = [0] * N
        stack = []

        for i, t in enumerate(tmps):

            while stack and stack[-1][0] < t:
                prev_t, j = stack.pop()
                res[j] = i - j

            stack.append((t, i))

        return res