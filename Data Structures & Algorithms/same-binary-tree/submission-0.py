# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def dfs(p, q):
            
            # base case
            if not p and not q:
                return True

            if not p or not q:
                return False

            left = dfs(p.left, q.left)
            if not left:
                return False

            right = dfs(p.right, q.right)
            if not right:
                return False

            return p.val == q.val
        
        return dfs(p, q)