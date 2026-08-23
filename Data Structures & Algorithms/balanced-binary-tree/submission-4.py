# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True
        def dfs(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0
            if abs(dfs(node.left) - dfs(node.right)) > 1:
                self.balanced = False
            return 1 + max(dfs(node.left), dfs(node.right))
        dfs(root)
        return self.balanced