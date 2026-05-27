class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return [[""]]

        freq_map = {}

        for s in strs:
            key = [0] * 26

            for c in s:
                key[ord(c) - ord('a')] += 1
            
            if tuple(key) not in freq_map:
                freq_map[tuple(key)] = []
                freq_map[tuple(key)].append(s)
            else:
                freq_map[tuple(key)].append(s)
            
        return [strings for strings in freq_map.values()]