class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # dijkstra's to find the minimum cost

        # build the graph using adjacent list
        graph = defaultdict(list)
        for u, v, t in times:
            graph[u].append((v, t))
        
        # create variables
        min_heap = [] # [(time, node), ...]
        shortest_path = {} # {node: shortest time, ...}

        # enque the first node
        heapq.heappush(min_heap, (0, k))

        # bfs
        while min_heap: 
            # read the tuple pop from the min_heap since we aleays want to prioritize the shortest path
            time, node = heapq.heappop(min_heap)
            # if node has already been recorded with the shortest_path, we skip
            if node in shortest_path:
                continue
            # record the node in the shortest_path with the updated time
            shortest_path[node] = time
            # loop thru it's children, enque them with the time added up
            for child, cost in graph[node]:
                if child not in shortest_path:
                    heapq.heappush(min_heap, (time + cost, child))
    # check if all node are visited
        if len(shortest_path) == n:
        # if yes, return the max value among the shortes_path
            return max(shortest_path.values())
        else:
        # else return -1 to indicate that it's impossible to reach all the node
            return -1