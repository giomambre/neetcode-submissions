class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = [nums[i] for i in range(len(nums))]
        heapq.heapify_max(max_heap)
        
        for i in range(k):
            cur_max = heapq.heappop_max(max_heap)
        
        return cur_max