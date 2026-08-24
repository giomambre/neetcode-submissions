class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        cur = []

        def backTracking(i, s):
            if s == target:
                res.append(cur.copy())
                return

            if i >= len(nums) or s > target:
                return

            cur.append(nums[i])
            backTracking(i, s + nums[i])

            # undo
            cur.pop()

            # non scegliere nums[i], passa al prossimo
            backTracking(i + 1, s)

        backTracking(0, 0)
        return res