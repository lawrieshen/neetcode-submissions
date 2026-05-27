class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        freq_counter = [0] * 26
        max_freq = 0
        result = 1
        left = 0 

        for right in range(n):
            currentChar = ord(s[right]) - ord('A')
            freq_counter[currentChar] += 1
            max_freq = max(max_freq, freq_counter[currentChar])

            while (right - left + 1) > max_freq + k:
                charToBeRemoved = ord(s[left]) - ord('A')
                freq_counter[charToBeRemoved] -= 1
                left += 1

            result = max(result, right - left + 1)

        return result