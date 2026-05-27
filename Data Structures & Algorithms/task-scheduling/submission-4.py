class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = defaultdict(int)
        for task in tasks:
            counter[task] += 1
        
        maxf = max(counter.values())
        maxTasks = 0
        for count in counter.values():
            maxTasks += 1 if count == maxf else 0

        time = (maxf - 1) * (n + 1) + maxTasks

        return max(len(tasks), time)
