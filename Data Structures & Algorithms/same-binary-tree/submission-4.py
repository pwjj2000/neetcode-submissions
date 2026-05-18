# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        q1, q2 = [p], [q]
        while q1 and q2:
            n1, n2 = q1.pop(0), q2.pop(0)
            if n1 is None and n2 is None:
                continue
            if n1 is None or n2 is None or n1.val != n2.val:
                return False
            if n1.left and n2.left is None:
                return False
            if n1.right and n2.right is None:
                return False
            if n2.left and n1.left is None:
                return False
            if n2.right and n1.right is None:
                return False
            if n1.left:
                q1.append(n1.left)
                q2.append(n2.left)
            if n1.right:
                q1.append(n1.right)
                q2.append(n2.right)
        return len(q1) + len(q2) == 0