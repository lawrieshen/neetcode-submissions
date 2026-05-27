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
        j = 0 # length of current matched prefix

        for i in range(1, len(pattern)):
            while j > 0 and pattern[i] != pattern[j]:
                j = lps[j - 1]
            
            if pattern[i] == pattern[j]:
                j += 1
                lps[i] = j

        return lps

    def kmp_search(self, text: str, pattern: str) -> bool:
        if pattern == "":
            return True
        if text == "":
            return False

        lps = self.build_lps(pattern)
        j = 0 # index in pattern
        
        for i in range(len(text)):
            while j > 0 and text[i] != pattern[j]:
                j = lps[j - 1]
            if text[i] == pattern[j]:
                j += 1
                if j == len(pattern):
                    return True

        return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        serialized_root = self.serialize(root)
        serialized_sub = self.serialize(subRoot)
        return self.kmp_search(serialized_root, serialized_sub)