class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        p_queue = deque()
        p_seen = set()

        a_queue = deque()
        a_seen = set()

        m, n = len(heights), len(heights[0])

        for i in range(m):
            p_queue.append((i, 0))
            p_seen.add((i, 0))

            a_queue.append((i, n - 1))
            a_seen.add((i, n - 1))

        for j in range(n):
            p_queue.append((0, j))
            p_seen.add((0, j))

            a_queue.append((m - 1, j))
            a_seen.add((m - 1, j))

        def bfs(queue, seen):
            while queue:
                x, y = queue.popleft()

                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and heights[x][y] <= heights[nx][ny] and (nx, ny) not in seen:
                        seen.add((nx, ny))
                        queue.append((nx, ny))

        bfs(p_queue, p_seen)
        bfs(a_queue, a_seen)

        return list(p_seen & a_seen)

        

            