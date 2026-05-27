class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        p_que = deque()
        p_seen = set()

        a_que  = deque()
        a_seen = set()

        m, n = len(heights), len(heights[0])

        for j in range(n):
            p_que.append((0, j))
            p_seen.add((0, j))

            a_que.append((m - 1, j))
            a_seen.add((m - 1, j))

        for i in range(m):
            p_que.append((i, 0))
            p_seen.add((i, 0))

            a_que.append((i, n - 1))
            a_seen.add((i, n - 1))

        def bfs(queue, seen):
            cells = set()

            while queue:
                x, y = queue.popleft()
                
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and heights[x][y] <= heights[nx][ny] and (nx, ny) not in seen:
                        seen.add((nx, ny))
                        queue.append((nx, ny))
        
        bfs(p_que, p_seen)
        bfs(a_que, a_seen)

        return list(p_seen & a_seen)
