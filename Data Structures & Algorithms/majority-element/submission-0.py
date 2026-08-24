class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        goal = math.ceil(len(nums) /2)
        print (goal)
        map = defaultdict(int)
        for n in nums:
            map[n] +=1
            if map[n] == goal:
                return n
        
        return 0