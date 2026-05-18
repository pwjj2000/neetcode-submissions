# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.curr = 0
        def inorder(node):
            if node.left:
                inorder(node.left)
            self.curr += 1
            if self.curr == k:
                self.val = node.val
            if node.right:
                inorder(node.right)
        inorder(root)
        return self.val
            