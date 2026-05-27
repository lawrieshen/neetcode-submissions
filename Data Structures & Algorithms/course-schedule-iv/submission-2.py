class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # graph[v] = list of immediate prerequisites (parents) of v
        graph = defaultdict(list)
        for u, v in prerequisites:
            graph[v].append(u)

        # dp[u][v] = is u a (indirect or direct) prerequisite of v?
        dp = [[None] * numCourses for _ in range(numCourses)]
        for u, v in prerequisites:
            dp[u][v] = True # direct prerequisite

        # return true if and only if u is a prerequisite of v
        def dfs(u, v) -> bool:
            # check dp first
            if dp[u][v] != None:
                return dp[u][v]

            # unpack v into its prerequisites and check if u is among it; if not, we dive into recurrion
            for prerequisite_of_v in graph[v]:
                if prerequisite_of_v == u or dfs(u, prerequisite_of_v): # a is pre of b; b is pre of c -> a is pre of c
                    dp[prerequisite_of_v][v] = True                     # u is pre of p_v ; p_v is pre of v -> u is pre of v
                    return True

            dp[u][v] = False
            return False

        results = []
        for u, v in queries:
            results.append(dfs(u, v))
        return results

        
        