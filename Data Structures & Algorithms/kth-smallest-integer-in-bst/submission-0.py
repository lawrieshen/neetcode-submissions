# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1
        
        self.countdown = k
        self.result = None

        def inorder(node):
            if not node or self.result:
                return
            
            inorder(node.left)

            # process the node
            self.countdown -= 1
            if self.countdown == 0:
                self.result = node.val
                return

            inorder(node.right)
        
        inorder(root)
        return self.result

