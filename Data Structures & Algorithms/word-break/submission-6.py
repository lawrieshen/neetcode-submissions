class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        trie = Trie()
        for w in wordDict:
            trie.addWord(w)
        for i in range(len(s) - 1, -1, -1):
            cur = trie.root
            for j in range(i, len(s)):
                if s[j] not in cur.children:
                    break
                cur = cur.children[s[j]]
                if cur.isWord:
                    dp[i] = dp[j + 1]
                    if dp[i]:
                        break
        
        return dp[0]
