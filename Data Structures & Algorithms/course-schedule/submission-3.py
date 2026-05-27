class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not numCourses or not prerequisites:
            return True

        # build a graph
        graph = defaultdict(list)
        for course, prerequisite in prerequisites:
            graph[course].append(prerequisite)

        UNVISITED = 0
        VISITING = 1
        VISITED = 2

        states = [UNVISITED] * numCourses

        # run a dfs
        def dfs(course):
            if states[course] == VISITING:
                return False

            if states[course] == VISITED:
                return True

            states[course] = VISITING

            for child in graph[course]:
                if not dfs(child):
                    return False

            states[course] = VISITED

            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True