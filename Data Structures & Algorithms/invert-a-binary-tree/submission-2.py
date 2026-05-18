# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invert(node):
            if node is None:
                return None
            new_left, new_right = invert(node.right), invert(node.left)
            node.left, node.right = new_left, new_right
            return node
        return invert(root)