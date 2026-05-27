# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def serialize(self, root: Optional[TreeNode]) -> str:
        if root == None:
            return "$#"

        return ("$" + str(root.val) + self.serialize(root.left) + self.serialize(root.right))

    def build_lps(self, pattern: str) -> list[int]:
        lps = [0] * len(pattern)
        prevLPS, i = 0, 1

        while i < len(pattern):
            if pattern[i] == pattern[prevLPS]:
                lps[i] = prevLPS + 1
                prevLPS += 1
                i += 1
            else:
                if prevLPS == 0:
                    lps[i] = 0
                    i += 1
                else:
                    prevLPS = lps[prevLPS - 1]

        return lps

    def kmp_search(self, text: str, pattern: str) -> bool:
        if pattern == "":
            return True
        if text == "":
            return False

        lps = self.build_lps(pattern)
        i = 0 # pointer for text
        j = 0  # pointer for pattern

        while i < len(text):
            if text[i] == pattern[j]:
                i += 1
                j += 1
            else:
                if j == 0:
                    i += 1
                else:
                    j = lps[j - 1]

            if j == len(pattern):
                return True

        return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        serialized_root = self.serialize(root)
        serialized_sub = self.serialize(subRoot)
        return self.kmp_search(serialized_root, serialized_sub)