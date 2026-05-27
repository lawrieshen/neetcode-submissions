class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        max_heap = [-cnt for cnt in counter.values()]
        heapq.heapify(max_heap)

        time = 0
        cool_down = deque() #(-cnt, idleTime)
        while max_heap or cool_down:
            time += 1

            if max_heap:
                neg_cnt = 1 + heapq.heappop(max_heap)
                if neg_cnt:
                    cool_down.append([neg_cnt, time + n])
            else:
                time = cool_down[0][1]

            if cool_down and time == cool_down[0][1]:
                heapq.heappush(max_heap, cool_down.popleft()[0])

        return time


