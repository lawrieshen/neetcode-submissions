# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []

        queue = deque([root])

        while queue:
            size = len(queue)
            cache = []

            for _ in range(size):
                node = queue.popleft()
                if node:
                    cache.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)

            if cache:
                res.append(cache)

        return res

