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

        # the first item in the preorder tree is always the root
        root_val = preorder[0]
        root = TreeNode(root_val)

        # the index of root in inorder helps us divide the left subtree and right subtree
        root_index = inorder.index(root.val)

        # construct the tre recussively
        root.left = self.buildTree(preorder[1:root_index + 1], inorder[:root_index])
        root.right = self.buildTree(preorder[root_index + 1:], inorder[root_index + 1:]) 

        return root