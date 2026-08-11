class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = [[] for _ in range(numCourses)]
        isPrereq = [[-1] * numCourses for _ in range(numCourses)]
        for u, v in prerequisites:
            adj[u].append(v)
            isPrereq[u][v] == True

        def dfs(node, target):
            if isPrereq[node][target] != -1:
                return isPrereq[node][target] == 1

            if node == target:
                isPrereq[node][target] = 1
                return True

            for nei in adj[node]:
                if dfs(nei, target):
                    isPrereq[nei][target] = 1
                    return True

            isPrereq[node][target] = 0
            return False

        answer = []
        for u, v in queries:
            answer.append(dfs(u, v))
        return answer

            