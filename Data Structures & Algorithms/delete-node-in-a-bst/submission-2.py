# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root

        parent = None
        cur = root

        # Find the node to delete
        while cur and cur.val != key:
            # we also keep track of parent as well
            parent = cur
            if key > cur.val:
                cur = cur.right
            else:
                cur = cur.left

        if not cur:
            # if we find no node in the tree, we return the root to terminate the func
            return root

        # curr == node

        # Node with only one child or no child
        if not cur.left or not cur.right:
            child = cur.left if cur.left else cur.right

            if not parent: # if we are deleting the root node, we just return the child node as it's implicitly pruned
                return child

            # remove the curr (node we r deleting) from the chain of partent and the child node (left/right)
            if parent.left == cur:
                parent.left = child
            else:
                parent.right = child
        
        # Node with two children -> replace the node we r deleting with the min mode int he right sub tree
        else:
            par = None  # parent of right subTree min node
            delNode = cur
            cur = cur.right # mode the cursor to right sub tree
            
            while cur.left: # traverse to the leftmost 
                par = cur
                cur = cur.left
            
            # cur := the leftmost node in the right subTree (or the root of the right sub tree) 
            
            if par:  # if there was at least one left traversal -> we extract the leftmost node we want to replace with
                par.left = cur.right
                cur.right = delNode.right # attach the right sub tree to the leftmost node

            cur.left = delNode.left  # attach the lefr subtree to the left most node
            
            # upper
            # |
            # V
            # del
            # |
            # V
            #lower

            if not parent: 
                return cur

            if parent.left == delNode:
                parent.left = cur
            else:
                parent.right = cur

        return root