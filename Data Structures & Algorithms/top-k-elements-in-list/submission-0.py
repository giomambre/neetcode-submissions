class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = defaultdict(int)
        heap = []
        res = []
        for n in nums:
            map[n] += 1
        
        for p,v in map.items():
            heapq.heappush(heap,(-v,p))
        print(heap)
        for _ in range(k):
            v , f = heapq.heappop(heap)
            res.append(f)
        return res
