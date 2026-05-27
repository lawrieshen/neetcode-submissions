class Solution:
    def minWindow(self, s: str, t: str) -> str:
        len_s = len(s)
        len_t = len(t)
        t_count = Counter(t)
        required = len(t_count)
        left = right = 0
        formed = 0
        window_count = {}
        min_length = float('inf')
        min_window = (0, 0)

        while right < len_s:
            char = s[right]
            window_count[char] = window_count.get(char, 0) + 1

            if char in t and window_count[char] == t_count[char]:
                formed += 1

            while left <= right and formed == required:
                outgoing_char = s[left]

                # update length
                window_size = right - left + 1
                if window_size < min_length:
                    min_length = window_size
                    min_window = (left, right)

                # update counters and formed
                window_count[outgoing_char] -= 1
                if outgoing_char in t and window_count[outgoing_char] < t_count[outgoing_char]:
                    formed -= 1

                left += 1
            
            right += 1

        l, r = min_window

        return s[l:r + 1] if min_length != float('inf') else ""
        