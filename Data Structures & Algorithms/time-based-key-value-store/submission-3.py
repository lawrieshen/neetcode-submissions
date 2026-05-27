class TimeMap:

    def __init__(self):
        self.look_up = {} # {key: [(t, v)]}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.look_up:
            self.look_up[key] = []

        self.look_up[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.look_up:
            return ""

        vals = self.look_up[key]
        if not vals:
            return ""

        # use binary search to find the most rightmost pair whose t <= timestamp
        l = 0
        r = len(vals) - 1

        while l <= r:
            m = l + (r - l) // 2
            if vals[m][0] > timestamp:
                r = m - 1
            else:
                l = m + 1

        return "" if r == -1 else vals[r][1]