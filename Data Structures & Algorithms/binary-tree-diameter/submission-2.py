# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.longest = 0
        def dfs(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0
            if dfs(node.left) + dfs(node.right) > self.longest:
                self.longest = dfs(node.left) + dfs(node.right)
            return 1 + max(dfs(node.left), dfs(node.right))
        dfs(root)
        return self.longest
        