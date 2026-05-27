# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = deque([(root, 0)])
        max_depth = float('-inf')

        while queue:
            node, depth = queue.pop()
            max_depth = max(max_depth, depth)

            if not node:
                continue

            queue.append((node.left, depth + 1))
            queue.append((node.right, depth + 1))

        return max_depth