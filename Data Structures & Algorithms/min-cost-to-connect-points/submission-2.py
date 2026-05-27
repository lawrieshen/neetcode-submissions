class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # prim's optimal
        # Running Prim with:
        # minCost[v] = best known cost to connect v to the current tree, a visited set,
        # each iteration: linearly scan all unvisited v to pick the smallest minCost[v] (O(n)), 
        # then update all v with min(minCost[v], dist(u,v)) (O(n)).
        # Total n iterations ⇒ O(n²).

        n = len(points)

        min_cost = [float('inf')] * n
        min_cost[0] = 0

        unvisited = set(range(n))
        total_distance = 0
        
        while unvisited:
            # inearly scan all unvisited v to pick the smallest minCost[v]
            u = min(unvisited, key=lambda i: min_cost[i])

            unvisited.remove(u)
            total_distance += min_cost[u]
            
            # update all unvisited v with min(min_cost[v], dist(u, v))
            u_x, u_y = points[u]
            for v in unvisited:
                v_x, v_y = points[v]
                distance = abs(u_x - v_x) + abs(u_y - v_y)
                min_cost[v] = min(min_cost[v], distance)
        
        return total_distance
        