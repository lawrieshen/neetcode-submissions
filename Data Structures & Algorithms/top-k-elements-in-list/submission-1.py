class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)

        # bucket sort (where index is freq)
        max_freq = max(counter.values())
        buckets = [[] for _ in range(max_freq + 1)]

        for num, freq in counter.items():
            buckets[freq].append(num)
        
        result = []
        for freq in range(max_freq, 0, -1):
            for num in buckets[freq]:
                result.append(num)
                if len(result) >= k:
                    return result