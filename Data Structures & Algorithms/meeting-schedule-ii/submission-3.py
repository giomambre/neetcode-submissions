"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        events = []

        for interval in intervals:
            events.append((interval.start, 1))
            events.append((interval.end, -1))
        res = 0
        events.sort()
        cur = 0
        for ts,event in events:
            cur +=  event
            res = max(res,cur)
        
        return res