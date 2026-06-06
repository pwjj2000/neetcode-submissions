# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        q = deque([(root, -1001, 1001)])
        while q:
            node, mini, maxi = q.popleft()
            if node.val <= mini or node.val >= maxi:
                return False
            if node.left:
                q.append((node.left, mini, min(node.val, maxi)))
            if node.right:
                q.append((node.right, max(mini, node.val), maxi))
        return True