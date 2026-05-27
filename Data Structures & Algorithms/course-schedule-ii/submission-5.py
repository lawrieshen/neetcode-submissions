class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # build graph with adjacent list
        graph = defaultdict(list)
        for course, prerequisite in prerequisites:
            graph[course].append(prerequisite)
        
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

            for preq in graph[course]:
                if not dfs(preq):
                    return False
            
            states[course] = VISITED
            result.append(course)
            
            return True

        # execute dfs
        for i in range(numCourses):
            if not dfs(i):
                return []
        return result # this will be starting with the course which has no preq