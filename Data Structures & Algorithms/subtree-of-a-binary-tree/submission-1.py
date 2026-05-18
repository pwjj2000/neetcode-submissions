# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def same(p, q):
            if not p and not q:
                return True
            if not p or not q or p.val != q.val:
                return False
            return same(p.left, q.left) and same(p.right, q.right)
        
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if same(node, subRoot):
                return True
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return False