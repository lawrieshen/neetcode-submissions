# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        # the first item in the preorder is always the root
        root_val = preorder[0]
        root = TreeNode(root_val)
        # the index of root in inorder helps us divide the left tree and right tree
        root_index = inorder.index(root_val)

        # construct the tree recurrsively
        root.left = self.buildTree(preorder[1:root_index + 1], inorder[:root_index])
        root.right =self.buildTree(preorder[root_index + 1:], inorder[root_index + 1:])

        return root