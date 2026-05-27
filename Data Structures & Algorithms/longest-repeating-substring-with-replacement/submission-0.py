class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        left = 0
        counter = [0] * 26
        max_freq = 0

        for right in range(n):
            currentChar = ord(s[right]) - ord('A')
            counter[currentChar] += 1
            max_freq = max(max_freq, counter[currentChar])

            window_size = right - left + 1
            if window_size > max_freq + k:
                charToBeRemoved = ord(s[left]) - ord('A')
                counter[charToBeRemoved] -= 1
                left += 1
            
            result = right - left + 1

        return result