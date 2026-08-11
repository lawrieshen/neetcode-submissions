class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS, COLS = len(heights), len(heights[0])
        min_heap = [(0, 0, 0)] # (diff, row, col])
        visit = set()
        directions = [
            (0, 1),
            (1, 0),
            (0, -1),
            (-1, 0)
        ]

        while min_heap:
            diff, r, c = heapq.heappop(min_heap)

            if (r, c) in visit:
                continue

            visit.add((r, c))

            if (r, c) == (ROWS - 1, COLS - 1):
                return diff

            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS:
                    continue

                new_diff = max(diff, abs(heights[r][c] - heights[nr][nc]))
                heapq.heappush(min_heap, (new_diff, nr, nc))

        return 0

        # O(V * logV) we traverse throug each node in the graph and each traverse we perform a heapq operation costing logV