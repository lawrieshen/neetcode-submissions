class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # count frequency of each map
        freq_map = [0] * 26
        for task in tasks:
            freq_map[ord(task) - ord("A")] += 1

        # find the most frequent task using max heap
        max_heap = []
        for freq in freq_map:
            if freq > 0:
                heapq.heappush(max_heap, -freq)
        
        time = 0
        queue = deque()

        # simulamtion
        while max_heap or queue:
            time += 1

            if max_heap:
                freq = -heapq.heappop(max_heap) - 1
                if freq > 0:
                    queue.append((time + n, freq))

            if queue and queue[0][0] == time:
                # idle time end, add it back to heap
                heapq.heappush(max_heap, -queue.popleft()[1])

        return time
            