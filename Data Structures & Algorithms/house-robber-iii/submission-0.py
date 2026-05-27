# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        # sub problom optimistically find the max profit in one path

        # transition: at each node we decide if we wit
        # each sub tree has two different options 1. with root 2. without root
        # compared to find the max
        def dfs(root: TreeNode) -> List[int]:
            if not root:
                return [0, 0]

            left_amount = dfs(root.left) #[0, 0]
            right_amount = dfs(root.right) #[0, 0]

            withRoot = root.val + left_amount[1] + right_amount[1]
            withoutRoot = max(left_amount) + max(right_amount)


            return [withRoot, withoutRoot]

        return max(dfs(root))