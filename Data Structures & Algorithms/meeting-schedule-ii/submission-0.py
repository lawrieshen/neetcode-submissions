"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # sort rooms based on start tme
        intervals.sort(key=lambda x: x.start)

        # intialize the min-heap
        # this min-heap represent the room we are currently using
        # and it is prioritised by the end time coz if we want to check if we need to free/add a room, we always check the earlist ending one
        min_heap = []
        max_rooms = 0

        # we loop thru intervals; for each interval we check if current.start is >= min_heap[0].end
        # while current.start >= min_heap[0].end we don't need to add new room and we need to free room
        # we update the min_heap with rooms we are currently in use
        for interval in intervals:
            
            while min_heap and interval.start >= min_heap[0]:
                heapq.heappop(min_heap)

            heapq.heappush(min_heap, interval.end)
            max_rooms = max(max_rooms, len(min_heap))

        return max_rooms
            
