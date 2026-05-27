class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        wordSet = set(wordList)
        beginSet = {beginWord}
        endSet = {endWord}
        visited = set()
        depth = 1

        while beginSet and endSet:
            # Always expand the smaller for efficiency
            if len(beginSet) > len(endSet):
                beginSet, endSet = endSet, beginSet

            nextSet = set()
            for word in beginSet:
                for i in range(len(word)):
                    for char in set('abcdefghijklmnopqrstuvwxyz'):
                        transformed = word[:i] + char + word[i + 1:]
                        if transformed in endSet:
                            return depth + 1
                        if transformed in wordSet and transformed not in visited:
                            visited.add(transformed)
                            nextSet.add(transformed)

            beginSet = nextSet
            depth += 1

        return 0