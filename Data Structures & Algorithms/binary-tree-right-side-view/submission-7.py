# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        curr, queue = 0, [(root, 0)]
        answer = []
        while queue:
            node, d = queue.pop(0)
            if curr == d:
                answer.append(node.val)
                curr += 1
            if node.right:
                queue.append((node.right, d + 1))
            if node.left:
                queue.append((node.left, d + 1))
        return answer
        