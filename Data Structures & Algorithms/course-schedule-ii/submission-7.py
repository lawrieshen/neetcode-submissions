class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not numCourses:
            return []

        if not prerequisites:
            return [i for i in range(numCourses)]

        graph = defaultdict(list)
        for prerequisite, course in prerequisites:
            graph[course].append(prerequisite)

        UNVISITED = 0
        VISITING = 1
        VISITED = 2
        states = [UNVISITED] * numCourses

        result = []

        def dfs(course):
            if states[course] == VISITING:
                return False

            if states[course] == VISITED:
                return True

            states[course] = VISITING

            for prerequisite in graph[course]:
                if not dfs(prerequisite):
                    return False

            states[course] = VISITED
            result.append(course)

            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        
        result.reverse()
        return result

        