class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        heap = []
        count_map = {}
        for n in nums:
            if n not in count_map:
                count_map[n] =1 
            else:
                count_map[n] += 1

        for num, freq in count_map.items():

            if len(heap) < k:
                heapq.heappush(heap, (freq, num))
            elif heap[0][0] < freq:
                heapq.heappop(heap)
                heapq.heappush(heap, (freq, num))
    

        return [x[1] for x in heap]

