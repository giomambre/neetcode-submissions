class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        N = len(nums)//3
        mapToCount = defaultdict(int)
        res = set()
        for n in nums:
            mapToCount[n]+=1
            if mapToCount[n] > N:
                res.add(n)
        
        return list(res)