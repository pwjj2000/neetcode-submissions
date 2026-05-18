# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot is None:
            return True
        if root is None:
            return False
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node.val != subRoot.val:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                continue
            q1, q2 = [node], [subRoot]
            isDifferent = False
            while q1 and q2:
                n1, n2 = q1.pop(0), q2.pop(0)
                if n1.val != n2.val:
                    isDifferent = True
                if n1.left and n2.left is None:
                    isDifferent = True
                if n1.right and n2.right is None:
                    isDifferent = True
                if n2.left and n1.left is None:
                    isDifferent = True
                if n2.right and n1.right is None:
                    isDifferent = True
                if isDifferent:
                    break
                if n1.left:
                    q1.append(n1.left)
                    q2.append(n2.left)
                if n1.right:
                    q1.append(n1.right)
                    q2.append(n2.right)

            if len(q1) + len(q2) == 0 and not isDifferent:
                return True
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return False
        
        