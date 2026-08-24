class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = set()
        N = len(nums)

        def backT(curr):
            if len(curr) == N:
                res.append(curr.copy())
                return

            for j in range(N):
                if j in used:
                    continue

                used.add(j)
                curr.append(nums[j])

                backT(curr)

                curr.pop()
                used.remove(j)

        backT([])
        return res