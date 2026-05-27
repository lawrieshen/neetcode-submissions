class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # if 0000 is a deadend return -1
        # initialize a queue with the starting state 0000 and 0 turns
        # add all deadends to a visited set
        # while the queue is not empty:

            # dequeue a combination and its turn count
            # if it matches the target we return the turn count
            # generate all 8 neighbors (each wheel can go up or down)
            # for each unvisited neighbor, mark it visited, enqueue them with turn count + 1

        def generateChildren(lock: str) -> List[str]:
            res = []
            for i in range(4):
                digit = str((int(lock[i]) + 1) % 10)
                res.append(lock[:i] + digit + lock[i+1:])
                digit = str((int(lock[i]) - 1) % 10)
                res.append(lock[:i] + digit + lock[i+1:])
            return res
        
        if '0000' in deadends:
            return -1

        visited = set(deadends)
        visited.add('0000')
        queue = deque([('0000', 0)])

        while queue:
            lock, turns = queue.popleft()
            if lock == target:
                return turns

            for child in generateChildren(lock):
                if child not in visited:
                    visited.add(child)
                    queue.append((child, turns + 1))

        return -1

