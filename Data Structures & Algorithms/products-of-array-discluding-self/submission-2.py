class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        pref = [1]*N
        suff = [1]*N
        
        for i in range(1,N,1):
            pref[i] =nums[i-1]* pref[i-1]
        for i in range(N - 2, -1, -1):
            suff[i] =nums[i+1]* suff[i + 1]
        res = []

        for i in range(N):
                res.append(pref[i]*suff[i])
        return res