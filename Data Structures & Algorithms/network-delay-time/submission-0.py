class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # dijkstra's algorithm to find the shortest path from a source to destination
        
        # Step 1: Build adjancency list for graph representation
        graph = defaultdict(list)
        for u, v, t in times:
            graph[u].append((v, t))

        # Step 2: Dijkstra's algo based on min-heap
        min_heap = [(0, k)] # (time, node) 
        shortest_time = {}

        while min_heap:
            time, node = heapq.heappop(min_heap)

            if node in shortest_time:
                continue

            shortest_time[node] = time

            for neighbor, weight in graph[node]:
                if neighbor not in shortest_time:
                    heapq.heappush(min_heap, (time + weight, neighbor))

        # Step 3: check if all nodes are visited
        if len(shortest_time) == n:
            return max(shortest_time.values())
        else:
            return -1

            
