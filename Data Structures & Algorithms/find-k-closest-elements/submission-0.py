class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # in a sorted array, the best k closest elements must form a contiguous block.

        # Binary search the left boundary of the size-k window

        # [L, L - k + 1]

        # valid L is from 0...n - k

        # distance from x to arr[mid] vs distance from arr[mid + k] to x

        # if arr[mid] is farther than arr[mid + k], shift the window to right; else just stay/ shift the window to the left
        l, r = 0, len(arr) - k

        while l < r:
            m = (l + r) // 2
            if x - arr[m] > arr[m + k] - x:
                l = m + 1
            else:
                r = m

        return arr[l: l + k]