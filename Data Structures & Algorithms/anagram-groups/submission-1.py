class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq_map = defaultdict(list)

        for string in strs:
            counter = [0]*26
            for c in string:
                counter[ord(c) - ord('a')] += 1
            freq_map[tuple(counter)].append(string)

        return [string for string in freq_map.values()]