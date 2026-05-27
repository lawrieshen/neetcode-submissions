class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Treat words as nodes in an implicit graph.
        # Two words are connected if they differ by exactly one letter.
        # We want the shortest transformation path from beginWord to endWord.
        
        # perform BFS to find tghe shortest path
        
        if endWord not in wordList:
            return 0
        
        patternToWord = defaultdict(list)
        for word in wordList:
            for i, c in enumerate(word):
                pattern = word[:i] + '*' + word[i + 1:]
                patternToWord[pattern].append(word)

        queue = deque([beginWord])
        visited = set([beginWord])
        length = 1

        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return length
                for i, c in enumerate(word):
                    pattern = word[:i] + '*' + word[i + 1:]
                    for neighbor in patternToWord[pattern]:
                        if neighbor not in visited:
                            queue.append(neighbor)
                            visited.add(neighbor)
            length += 1

        return 0

        
