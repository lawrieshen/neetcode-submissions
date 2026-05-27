# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p, q)]
        
        while stack:
            node_1, node_2 = stack.pop()

            if not node_1 and not node_2:
                continue
            
            if not node_1 or not node_2 or node_1.val != node_2.val:
                return False

            stack.append((node_1.left, node_2.left))
            stack.append((node_1.right, node_2.right))

        return True