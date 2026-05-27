class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda t: t[1]) # sort by starting time

        min_heap = [] # (end, passengers) to keep track of the current capacity being used, every time we checking of there any ongiing trip we prioritised the earlist end one
        curr_pass = 0

        for passengers, start, end in trips:

            # check if there are any ongoing trip, if not we need to decrease the curr_pass
            while min_heap and min_heap[0][0] <= start:
                _, prev_passengers = heapq.heappop(min_heap)
                curr_pass -= prev_passengers
            
            curr_pass += passengers
            if curr_pass > capacity:
                return False

            heapq.heappush(min_heap, (end, passengers))

        return True