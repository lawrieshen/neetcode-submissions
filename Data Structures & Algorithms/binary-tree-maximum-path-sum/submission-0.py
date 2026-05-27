# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.max_path_sum = float('-inf')

        def dfs(node):

            # base condition
            if not node:
                return 0

            # traversing
            left_path_sum = max(dfs(node.left), 0)
            right_path_sum = max(dfs(node.right), 0)

            current_path_sum = node.val + left_path_sum + right_path_sum

            self.max_path_sum = max(self.max_path_sum, current_path_sum)

            return node.val + max(left_path_sum, right_path_sum)

        dfs(root)

        return self.max_path_sum