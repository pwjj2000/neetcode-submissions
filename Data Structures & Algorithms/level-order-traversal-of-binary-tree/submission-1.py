# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        curr_depth = 0
        queue, answer = [(root, 0)], [[]]
        while queue:
            node, d = queue.pop(0)
            if d == curr_depth:
                answer[d].append(node.val)
            else:
                answer.append([])
                answer[d].append(node.val)
                curr_depth += 1
            if node.left:
                queue.append((node.left, d + 1))
            if node.right:
                queue.append((node.right, d + 1))
        return answer
