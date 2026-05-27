class TimeMap:

    def __init__(self):
        self.timestamp_lookup = defaultdict(list) # map key -> timestamp
        self.value_lookup = defaultdict(list) # map key -> val

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timestamp_lookup[key].append(timestamp)
        self.value_lookup[key].append(value)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.value_lookup:
            return ""
        
        timestamps = self.timestamp_lookup[key]
        left, right = 0, len(timestamps) - 1
        most_recent = -1

        # find most recent aka the rightmost
        while left <= right:
            mid = (left + right) // 2

            if timestamps[mid] <= timestamp:
                most_recent = mid
                # keeps exploring space with larger timestamps and see if exceed
                left = mid + 1
            else:
                right = mid - 1


        return self.value_lookup[key][most_recent] if most_recent != -1 else ""
