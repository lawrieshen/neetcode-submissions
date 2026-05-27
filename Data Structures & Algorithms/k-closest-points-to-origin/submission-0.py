class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [(x**2 + y**2, [x, y]) for x, y in points]
        heapq.heapify(heap)

        return [heapq.heappop(heap)[1] for _ in range(k)]