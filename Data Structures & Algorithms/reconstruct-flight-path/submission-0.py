class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # intuition: Eulerian Graph where visiting all nodews exatly once

        # build the graph, while maintaining its lexicographically order
        graph = defaultdict(list)
        for departure, arrival in tickets:
            heapq.heappush(graph[departure], arrival)
        
        itierary = []


        def dfs(airport):
            while graph[airport]:
                next_airport = heapq.heappop(graph[airport])
                dfs(next_airport)
            itierary.append(airport)
        
        dfs("JFK")

        return itierary[::-1]