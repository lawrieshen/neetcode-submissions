# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.pre_idx = 0
        self.in_idx = 0
        def dfs(limit):
            if self.pre_idx >= len(preorder):
                return None
            if inorder[self.in_idx] == limit:
                self.in_idx += 1
                return None

            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(root_val)
            root.left = dfs(root.val)
            root.right = dfs(limit)
            return root

        return dfs(float('inf'))
            