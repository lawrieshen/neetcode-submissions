class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # intuition: Eulerian Graph where we visiting all edges exatly once

        # build the graph, while maintaining its lexicographically order
        graph = defaultdict(list)
        for departure, arrival in tickets:
            heapq.heappush(graph[departure], arrival)
        
        itierary = []


        def eulerian(airport):
            while graph[airport]:
                next_airport = heapq.heappop(graph[airport]) # only visit this edge once, pop it and don't add it back!
                eulerian(next_airport)
            itierary.append(airport)
        
        eulerian("JFK")

        return itierary[::-1]