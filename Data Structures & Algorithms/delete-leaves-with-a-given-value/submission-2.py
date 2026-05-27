# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        # use dfs to traverse to the leaf node, then delete it

        #   3
        # null 3
        #.    3

        def dfs(node: TreeNode, target: int) -> TreeNode:
            if not node:
                return None

            node.left = dfs(node.left, target)

            node.right = dfs(node.right, target)

            if not node.left and not node.right and node.val == target:
                # we found leaf, remove it from the parent
                return None

            return node

        return dfs(root, target)

