class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create a frequency map
        freq_map = {}
        # loop thhrough the list
        for string in strs:
            key = [0] * 26
            
            for character in string:
                key[ord(character) - ord('a')] += 1

            if tuple(key) not in freq_map:
                freq_map[tuple(key)] = []
                freq_map[tuple(key)].append(string)
            else:
                freq_map[tuple(key)].append(string)

        return [string for string in freq_map.values()]

        # creat an unique key to represent the frequency of each letter with int the string

        # put each into the hash map;  hash map would do the grouping for us


        # return