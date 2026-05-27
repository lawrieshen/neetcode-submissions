class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_length = len(s1)
        s2_length = len(s2)

        if s1_length > s2_length:
            return False

        s1_count = Counter(s1)
        window_count = Counter(s2[:s1_length])
        
        if s1_count == window_count:
            return True

        for i in range(s1_length, s2_length):
            start_char = s2[i - s1_length]
            new_char = s2[i]

            window_count[start_char] -= 1
            window_count[new_char] += 1

            if window_count == s1_count:
                return True
        
        return False
