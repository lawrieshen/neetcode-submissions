class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # m = len(grid)
        # n = len(grid[0])
        # queue = deque()
        # fresh_count = 0
        # # find the rotten oranges
        # for i in range(m):
        #     for j in range(n):
        #         if grid[i][j] == 2:
        #             queue.append((i, j))
        #         elif grid[i][j] == 1:
        #             fresh_count += 1

        # # run bfs, everytime when we proceed to another level, we increase the timer
        # timer = 0
        # while queue:
        #     for _ in range(len(queue)):
        #         r, c = queue.popleft()
        #         for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        #             nr, nc = dr + r, dc + c
        #             if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
        #                 grid[nr][nc] = 2
        #                 fresh_count -= 1
        #                 queue.append((nr, nc))
        #     if len(queue) > 0:
        #         timer += 1
        
        # return timer if fresh_count == 0 else -1

        m = len(grid)
        n = len(grid[0])
        queue = deque()
        fresh_count = 0
        directions = [
            (0 ,1),
            (1, 0),
            (0, -1),
            (-1, 0)
        ]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh_count += 1
                if grid[i][j] == 2:
                    queue.append((i, j))

        timer = 0
        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = dx + x, dy + y
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                        grid[nx][ny] = '2'
                        fresh_count -= 1
                        queue.append((nx, ny))
            
            if len(queue) > 0:
                timer += 1

        return timer if fresh_count == 0 else -1
