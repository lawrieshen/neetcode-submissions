class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # if a task appears maxf times, these copies must be at least n units apart
        # this creats maxf - 1 gaps, and each gap must have a length of (n + 1) slots (the task itself and n cooldowns)
        # if multiples tasks share this maximum freq, they all occupy thie final row of the structure
        # counter = defaultdict(int)
        # for task in tasks:
        #     counter[task] += 1
        
        # maxf = max(counter.values())
        # maxTasks = 0
        # for count in counter.values():
        #     maxTasks += 1 if count == maxf else 0

        # time = (maxf - 1) * (n + 1) + maxTasks

        # return max(len(tasks), time)

        count = Counter(tasks)
        max_heap = [-cnt for cnt in count.values()]
        heapq.heapify(max_heap)

        time = 0
        q = deque() # pairs of [-cnt, idle_time]
        while max_heap or q:
            time += 1

            if not max_heap:
                time = q[0][1]
            else:
                cnt = 1 + heapq.heappop(max_heap)
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(max_heap, q.popleft()[0])

        return time