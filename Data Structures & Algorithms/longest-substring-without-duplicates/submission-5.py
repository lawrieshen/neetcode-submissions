class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        cache = set()
        left = 0
        longest = 0

        for right in range(n):
            c = s[right]

            while c in cache:
                cache.remove(s[left])
                left += 1

            cache.add(c)
            longest = max(longest, right - left + 1)

        return longest