# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # if not root or not p or not q:
        #     return None

        # if (max(p.val, q.val) < root.val):
        #     return self.lowestCommonAncestor(root.left, p, q)
        # elif (min(p.val, q.val) > root.val):
        #     return self.lowestCommonAncestor(root.right, p, q)
        # else:
        #     return root

        if not root or not p or not q:
            return None

        if max(p.val, q.val) < root.val:
            # ancestor in left subtree
            return self.lowestCommonAncestor(root.left, p, q)
        elif min(p.val, q.val) > root.val:
            # ancestor in right subtree
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            # ancestor is in between p and q trees! the first one we encounter while traversing down is what we want since it needs to be the lowest
            return root