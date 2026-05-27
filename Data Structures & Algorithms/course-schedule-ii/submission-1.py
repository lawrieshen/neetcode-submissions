class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # build graph with adjacent list
        graph = defaultdict(list)
        for dest, src in prerequisites:
            graph[src].append(dest)
        
        # varaiables
        states = [0] * numCourses
        UNVISITED = 0
        VISITING = 1
        VISITED = 2

        result = []

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
            result.append(course)
            
            return True

        # execute dfs
        for i in range(numCourses):
            if not dfs(i):
                return []

        return result[::-1]