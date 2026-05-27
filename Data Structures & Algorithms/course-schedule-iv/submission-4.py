class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        if not queries:
            return []

        graph = defaultdict(list)
        isPrereq = [[-1] * numCourses for _ in range(numCourses)]
        for prerequisite, course in prerequisites:
            graph[course].append(prerequisite)
            isPrereq[course][prerequisite] = 1

        def dfs(course, prereq):
            # if course == target:
            #     return True
            if isPrereq[course][prereq] != -1:
                return isPrereq[course][prereq] == 1

            for pre in graph[course]:
                if pre == prereq or dfs(pre, prereq):
                    isPrereq[course][prereq] = 1
                    return True

            isPrereq[course][prereq] = 0
            return False


        res = []
        for prerequisite, course in queries:
            res.append(dfs(course, prerequisite))
        return res

        # O((V + E) * Q)

            