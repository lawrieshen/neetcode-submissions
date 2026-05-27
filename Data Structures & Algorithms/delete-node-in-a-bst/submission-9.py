# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        parent =  None
        cur = root

        while cur and cur.val != key:
            parent = cur
            if key < cur.val:
                cur = cur.left
            else:
                cur = cur.right

        if not cur:
            return root

        if not cur.left or not cur.right:
            child = cur.left if cur.left else cur.right

            if not parent:
                return child
            
            if parent.left == cur:
                parent.left = child
            else:
                parent.right = child

        else:
            par = None
            delNode = cur
            cur = cur.right
            while cur.left:
                par = cur
                cur = cur.left

            if par:
                par.left = cur.right
                cur.right = delNode.right

            cur.left = delNode.left

            if not parent:
                return cur

            if parent.left == delNode:
                parent.left = cur
            else:
                parent.right = cur

        return root