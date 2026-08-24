class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map = defaultdict(int)

        for n in nums:
            if map[n] == 1:
                return True
            map[n]+=1
        return False
        