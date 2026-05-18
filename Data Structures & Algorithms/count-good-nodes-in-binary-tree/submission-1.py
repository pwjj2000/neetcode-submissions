# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.good = 0
        q = deque([(root, float('-inf'))])
        while q:
            node, maxi = q.popleft()
            if node.val >= maxi:
                self.good += 1
            maxi = max(node.val, maxi)
            if node.left:
                q.append((node.left, maxi))
            if node.right:
                q.append((node.right, maxi))
        return self.good