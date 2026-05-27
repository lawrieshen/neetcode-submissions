class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_end = False
        self.word = None

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        
        node.is_end = True
        node.word = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Step 1. Build a Trie
        trie = Trie()
        for word in words:
            trie.insert(word)

        # Step 2. Prepare DFS
        rows, cols = len(board), len(board[0])
        result = set()
        root = trie.root

        def dfs(r, c, node):
            char = board[r][c]
            if char not in node.children:
                return # prune search

            next_node = node.children[char]
            if next_node.is_end:
                result.add(next_node.word) # Found a word

            board[r][c] = '#' # Mark as visited

            # Proceed to next level
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != '#':
                    dfs(nr, nc, next_node)
            
            # restore
            board[r][c] = char
        
        # run through dfs
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)
        
        return list(result)

        # Complexity Analysis
        # Trie Construction: O(W * L) where W is the numner of words and L is the longest lenght among the word
        # DFS: O(R * C * 4^L) we traverse the whole board and at each cell we have at most 4 directions to explore
                
            
        