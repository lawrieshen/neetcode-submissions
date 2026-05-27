# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:

        if not root:
            return "[]"
        
        result = []
        queue = deque([root])
        
        while queue:
            node = queue.popleft()
            if node:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append("null")
        
        # Remove trailing 'null's for efficiency
        while result and result[-1] == "null":
            result.pop()
        
        return "[" + ",".join(result) + "]"

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:

        if data == "[]":
            return None
        
        nodes = data[1:-1].split(",")
        root = TreeNode(int(nodes[0]))
        queue = deque([root])
        
        i = 1
        while queue and i < len(nodes):
            node = queue.popleft()
            
            if nodes[i] != "null":
                node.left = TreeNode(int(nodes[i]))
                queue.append(node.left)
            i += 1
            
            if i < len(nodes) and nodes[i] != "null":
                node.right = TreeNode(int(nodes[i]))
                queue.append(node.right)
            i += 1
        
        return root
