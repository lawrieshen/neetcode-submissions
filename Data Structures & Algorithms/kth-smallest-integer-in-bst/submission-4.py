# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return 0

        self.res = None
        self.countdown = k

        def inorder(node):
            if not node:
                return

            inorder(node.left)
            self.countdown -= 1
            if self.countdown == 0:
                self.res = node.val
            inorder(node.right)

            return

        inorder(root)
        return self.res