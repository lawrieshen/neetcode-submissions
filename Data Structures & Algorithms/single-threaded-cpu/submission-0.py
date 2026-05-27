class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # Build indexed = [(enqueue, process, idx) ...], sort by enqueue.
        indexed = [(enqueue_time, processing_time, idx) for idx, (enqueue_time, processing_time) in enumerate(tasks)]
        indexed.sort(key=lambda x:x[0])
        # Init time = 0, i = 0, min_heap = [], res = [].
        time = 0
        i = 0
        min_heap = []
        res = []
        n = len(tasks)

        # While i < n or min_heap:
        while i < n or min_heap:
            # If not min_heap and time < indexed[i].enqueue: time = indexed[i].enqueue.
            if not min_heap and time < indexed[i][0]:
                time = indexed[i][0]            
            
            while i < n and indexed[i][0] <= time:
                heapq.heappush(min_heap, (indexed[i][1], indexed[i][2]))
                i += 1

            processing_time, idx = heapq.heappop(min_heap)
            time += processing_time
            res.append(idx)
            # Pop (proc, idx) from min_heap; time += proc; res.append(idx).

        # Return res.
        return res