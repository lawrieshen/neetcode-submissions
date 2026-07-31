class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        longest = 1
        l, r = 0, 0
        seen = {}

        while r < len(s):
            if s[r] in seen:
                l = max(seen[s[r]] + 1, l)
            
            seen[s[r]] = r
            longest = max(longest, r - l + 1)
            r += 1

        return longest