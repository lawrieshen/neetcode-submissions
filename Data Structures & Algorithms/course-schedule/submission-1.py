class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # build graph using adjacent list representation
        graph = defaultdict(list)
        for src, dest in prerequisites:
            graph[src].append(dest)

        # state machine
        states = [0] * numCourses
        UNVISITED = 0
        VISITING = 1
        VISITED = 2

        # dfs 
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