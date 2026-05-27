class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_counter = [0] * 26
        max_freq = 0
        left = 0
        result = 0

        for right in range(len(s)):
            index = ord(s[right]) - ord('A')
            freq_counter[index] += 1
            max_freq = max(max_freq, freq_counter[index])

            while (right - left + 1) > max_freq + k:
                left_index = ord(s[left]) - ord('A')
                freq_counter[left_index] -= 1
                left += 1

            result = max(result, right - left + 1)

        return result
