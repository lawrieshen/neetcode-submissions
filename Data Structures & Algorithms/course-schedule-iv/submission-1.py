class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # build the graph first
        graph = defaultdict(list)
        # precompute the reachability
        dp = [[-1] * numCourses for _ in range(numCourses)] #dp[i][j] -> course i to course j is reachable or not
        for preq, course in prerequisites:
            graph[course].append(preq)
            dp[preq][course] = True # direct result

        def dfs(course, preq):
            if dp[preq][course] != -1:
                return dp[preq][course]

            for pre in graph[course]:
                if pre == preq or dfs(pre, preq):
                    dp[preq][pre] = True
                    return True

            dp[preq][course] = False
            return False

        res = []
        for u, v in queries:
            res.append(dfs(v, u))

        return res

        
        