# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        queue = [(root, float('-inf'), float('inf'))]
        while queue:
            node, mini, maxi = queue.pop(0)
            if node.val <= mini or node.val >= maxi:
                return False
            if node.left:
                queue.append((node.left, mini, node.val))
            if node.right:
                queue.append((node.right, node.val, maxi))
        return True