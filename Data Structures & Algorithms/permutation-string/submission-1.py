class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_length = len(s1)
        s2_length = len(s2)

        if s1_length > s2_length:
            return False

        s1_counter = Counter(s1)
        window_counter = Counter(s2[:s1_length])

        if s1_counter == window_counter:
            return True

        for i in range(s1_length, s2_length):
            starting_char = s2[i - s1_length]
            new_char = s2[i]

            window_counter[starting_char] -= 1
            window_counter[new_char] += 1

            if s1_counter == window_counter:
                return True

        return False