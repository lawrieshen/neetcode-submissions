class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)

        if n1 > n2:
            return False

        counter1 = [0] * 26
        window = [0] * 26

        for i, c in enumerate(s1):
            index = ord(c) - ord('a')
            counter1[index] += 1
        
        for i in range(n1):
            c = s2[i]
            index = ord(c) - ord('a')
            window[index] += 1

        if counter1 == window:
            return True

        for i in range(n1, n2):
            starting_char = s2[i - n1]
            starting_char_index = ord(starting_char) - ord('a')
            new_char = s2[i]
            new_char_index = ord(new_char) - ord('a')
            
            window[starting_char_index] -= 1
            
            window[new_char_index] += 1

            if window == counter1:
                return True
            
            i += 1

        return False

        