# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []

        def dfs(node):
            if not node:
                res.append('N')
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return ','.join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        preorder = data.split(',')
        pre_idx = 0
        
        def dfs():
            nonlocal pre_idx
            if preorder[pre_idx] == 'N':
                pre_idx += 1
                return None

            node = TreeNode(preorder[pre_idx])
            pre_idx += 1
            node.left = dfs()
            node.right = dfs()

            return node

        return dfs()