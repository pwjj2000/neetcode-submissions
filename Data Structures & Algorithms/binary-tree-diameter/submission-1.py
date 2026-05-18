# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        def length(node):
            if not node or (not node.left and not node.right):
                return 0
            left_length = length(node.left) + 1 if node.left else 0
            right_length = length(node.right) + 1 if node.right else 0
            if left_length + right_length > self.diameter:
                self.diameter = left_length + right_length
            return max(left_length, right_length)
        length(root)
        return self.diameter