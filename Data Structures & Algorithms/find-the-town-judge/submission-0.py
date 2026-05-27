class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # the town judge has an indegree of n - 1 and outdegree of 0
        # we count the indegree and the outdegree for each person and find the one matchinf these criteria

        incoming = defaultdict(int)
        outgoing = defaultdict(int)

        for truster, trustee in trust:
            incoming[trustee] += 1
            outgoing[truster] += 1

        for i in range(1, n + 1):
            if incoming[i] == n - 1 and outgoing[i] == 0:
                return i

        return -1