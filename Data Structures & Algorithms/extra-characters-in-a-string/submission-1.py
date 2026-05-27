class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        # At each index in s, what is the minimum number of extra characters from here to the end?

        # try to match a dictionary word starting at position i
        # if you can match one, jump to the end of that word
        # if you cannot or choose not to use one, treat s[i] as an extra character and move to i + 1

        if not s:
            return 0

        if not dictionary:
            return len(s)

        n = len(s)

        trie = Trie()
        for word in dictionary:
            trie.insert(word)

        dp = [0] * (n + 1) # dp[i] define min characters starting from index; at the end we want dp[0]

        for i in range(n - 1, -1, -1):
            dp[i] = 1 + dp[i + 1]
            curr = trie.root
            for j in range(i, n):
                if s[j] not in curr.children:
                    break
                curr = curr.children[s[j]]
                if curr.isWord:
                    dp[i] = min(dp[i], dp[j + 1])

        return dp[0]

