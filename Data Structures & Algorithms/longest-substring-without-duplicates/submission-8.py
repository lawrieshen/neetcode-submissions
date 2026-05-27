class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        left = 0
        longest = 0
        seen = set()

        for right in range(n):
            c = s[right]

            while c in seen:
                seen.remove(s[left])
                left += 1

            seen.add(c)
            longest = max(longest, right - left + 1)

        return longest