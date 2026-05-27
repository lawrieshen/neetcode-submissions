class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        euclidean = lambda x: x[0] ** 2 + x[1] ** 2
        def partition(l, r):
            pivot_idx = r
            pivot_dist = euclidean(points[pivot_idx])
            i = l
            for j in range(l, r):
                if euclidean(points[j]) <= pivot_dist:
                    points[i], points[j] = points[j], points[i]
                    i += 1
            points[i], points[r] = points[r], points[i]
            return i

        L, R = 0, len(points) - 1

        while True:
            pivot = partition(L, R)
            if pivot == k - 1:
                break
            elif pivot < k - 1:
                L = pivot + 1
            else:
                R = pivot - 1
        return points[:k]