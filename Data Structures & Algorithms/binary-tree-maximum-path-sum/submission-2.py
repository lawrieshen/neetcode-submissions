# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # use dfs to traversr the tree, at each level, 
        # we update the current sum if the node is contribute negatively we remove it from current sum

        max_sum = float('-inf')

        def dfs(node):
            nonlocal max_sum

            if not node:
                return 0

            left_max = dfs(node.left)
            right_max = dfs(node.right)
            left_max = max(left_max, 0)
            right_max = max(right_max, 0)

            max_sum = max(max_sum, node.val + left_max + right_max)

            return node.val + max(left_max, right_max)

        dfs(root)
        return max_sum