"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        cloned_nodes = {}

        def dfs(node: Node):
            if node in cloned_nodes:
                return cloned_nodes[node]
            
            
            cloned_node = Node(node.val)
            cloned_nodes[node] = cloned_node

            for neighbor in node.neighbors:
                cloned_node.neighbors.append(dfs(neighbor))


            return cloned_node

        return dfs(node)