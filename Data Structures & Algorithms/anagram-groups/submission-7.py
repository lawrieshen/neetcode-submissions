class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cache = defaultdict(list)

        for string in strs:
            signature = [0] * 26

            for c in string:
                signature[ord(c) - ord('a')] += 1
            
            cache[tuple(signature)].append(string)

        return list(cache.values())
