class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if not points:
            return []

        max_heap = []
        for point in points:
            x, y = point
            distance = math.sqrt(x**2 + y**2)
            heapq.heappush(max_heap, (-distance, point))
            if len(max_heap) > k:
                heapq.heappop(max_heap)

        return [point for neg_distance, point in max_heap]