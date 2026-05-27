class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq_map = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            key = tuple(count)
            freq_map[key].append(s)

        return list(freq_map.values())