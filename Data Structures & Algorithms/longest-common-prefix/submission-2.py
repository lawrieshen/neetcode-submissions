class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]

        for s in strs:
            i = 0
            while i < min(len(prefix), len(s)):
                if (prefix[i] != s[i]):
                    break
                i += 1
            prefix = prefix[0:i]

        return prefix