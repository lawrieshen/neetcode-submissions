# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # run a dfs and passing the current maxima down.
        # at each recurssion if node.val > current maxima, it's a good node
        if not root:
            return 0
        
        count = 0
        def dfs(node, maxima):
            nonlocal count

            if not node:
                return

            if node.val >= maxima:
                count += 1

            maxima = max(maxima, node.val)
            dfs(node.left, maxima)
            dfs(node.right, maxima)
        
        dfs(root, float('-inf'))
        return count


            

            