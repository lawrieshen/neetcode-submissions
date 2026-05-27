class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Convert to a max-heap by pushing negative values
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)  # Efficiently create a heap in O(N)

        while len(max_heap) > 1:
            # Pop two largest stones
            x, y = -heapq.heappop(max_heap), -heapq.heappop(max_heap)

            if x != y:
                heapq.heappush(max_heap, -(x - y))  # Push the difference

        return -max_heap[0] if max_heap else 0  # Return the last stone or 0 if empty