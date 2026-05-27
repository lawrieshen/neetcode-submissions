# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.maxDiameter = float('-inf')

        def dfs(node):

            if not node:
                return 0

            left_height = dfs(node.left)
            right_height = dfs(node.right)

            self.maxDiameter = max(self.maxDiameter, left_height + right_height)
            
            return max(left_height, right_height) + 1

        dfs(root)

        return self.maxDiameter