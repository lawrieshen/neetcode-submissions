class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        indices = list(range(n))
        indices.sort(key=lambda i: (tasks[i][0], i))

        min_heap = [] # compares indices by their task's processing time (then by index for ties).
        res = []
        time = 0 
        i = 0

        while min_heap or i < n:
            # Push indices of tasks that have become available onto the heap.
            while i < n and tasks[indices[i]][0] <= time:
                heapq.heappush(min_heap, (tasks[indices[i]][1], indices[i]))
                i += 1
            # If the heap is empty and tasks remain, jump time forward.
            if not min_heap:
                time = tasks[indices[i]][0]
            # Otherwise, pop the best task, update time, and record the result.
            else:
                next_task = heapq.heappop(min_heap)
                time += next_task[0]
                res.append(next_task[1])

        return res