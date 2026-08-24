class MedianFinder:

    def __init__(self):
        self.L = []  # max heap
        self.R = []  # min heap

    def addNum(self, num: int) -> None:

        if not self.L or num <= self.L[0]:
            heapq.heappush_max(self.L, num)
        else:
            heapq.heappush(self.R, num)

        # balance
        if len(self.L) > len(self.R) + 1:
            val = heapq.heappop_max(self.L)
            heapq.heappush(self.R, val)

        elif len(self.R) > len(self.L):
            val = heapq.heappop(self.R)
            heapq.heappush_max(self.L, val)

    def findMedian(self) -> float:

        if len(self.L) > len(self.R):
            return self.L[0]

        return (self.L[0] + self.R[0]) / 2