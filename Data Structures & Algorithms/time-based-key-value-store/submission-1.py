class TimeMap:

    def __init__(self):
        self.timestamp_map = defaultdict(list)  # Stores timestamps for each key
        self.value_map = defaultdict(list)  # Stores values for each key in order of timestamps
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timestamp_map[key].append(timestamp)
        self.value_map[key].append(value)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timestamp_map:
            return ""

        timestamps = self.timestamp_map[key]
        left, right = 0, len(timestamps) - 1
        best_index = -1

        while left <= right:
            mid = (left + right) // 2
            if timestamps[mid] <= timestamp:  
                best_index = mid  # Store the largest timestamp ≤ given timestamp
                left = mid + 1  # Move right to find a later valid timestamp
            else:
                right = mid - 1  # Move left to search for a smaller timestamp

        return self.value_map[key][best_index] if best_index != -1 else ""