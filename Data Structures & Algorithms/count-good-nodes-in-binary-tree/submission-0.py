# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        answer = 0
        stack = [(root, float('-inf'))]
        while stack:
            node, maxi = stack.pop()
            if node.val >= maxi:
                answer += 1
                maxi = node.val
            if node.left:
                stack.append((node.left, maxi))
            if node.right:
                stack.append((node.right, maxi))
        return answer