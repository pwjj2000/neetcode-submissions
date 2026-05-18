# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count, self.res = 1, None
        def inorder(node):
            if node.left:
                inorder(node.left)
            if self.count == k:
                self.res = node.val
            self.count += 1
            if node.right:
                inorder(node.right)
        inorder(root)
        return self.res

            