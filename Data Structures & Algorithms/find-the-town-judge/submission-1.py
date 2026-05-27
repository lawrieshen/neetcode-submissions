class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # the town judge has an indegree of n - 1 and outdegree of 0
        # we count the indegree and the outdegree for each person and find the one matchinf these criteria

        delta = defaultdict(int)

        for truster, trustee in trust:
            delta[trustee] += 1
            delta[truster] -= 1

        for i in range(1, n + 1):
            if delta[i] == n - 1:
                return i

        return -1