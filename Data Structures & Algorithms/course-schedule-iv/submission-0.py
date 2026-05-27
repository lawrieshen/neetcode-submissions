class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # build the graph first
        graph = defaultdict(list)
        dp = [[-1] * numCourses for _ in range(numCourses)]
        for preq, course in prerequisites:
            graph[course].append(preq)
            dp[course][preq] = True # direct result

        def dfs(course, preq):
            if dp[course][preq] != -1:
                return dp[course][preq]

            for pre in graph[course]:
                if pre == preq or dfs(pre, preq):
                    dp[pre][preq] = True
                    return True

            dp[course][preq] = False
            return False

        res = []
        for u, v in queries:
            res.append(dfs(v, u))

        return res

        
        