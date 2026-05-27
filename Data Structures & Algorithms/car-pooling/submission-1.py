class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: x[1])

        prev_trips = [] #(end)
        curPass = 0
        
        for numPass, start, end in trips:
            while prev_trips and prev_trips[0][0] <= start:
                curPass -= heapq.heappop(prev_trips)[1]

            curPass += numPass
            if curPass > capacity:
                return False

            heapq.heappush(prev_trips, (end, numPass))

        return True
            
