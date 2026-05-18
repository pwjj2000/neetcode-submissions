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
        q = [(root, 0)]
        curr = 0
        arr, ans = [], []
        while q:
            node, lvl = q.pop(0)
            if curr != lvl:
                ans.append(arr)
                curr += 1
                arr = []
            arr.append(node.val)
            if node.left:
                q.append((node.left, lvl+1))
            if node.right:
                q.append((node.right, lvl+1))
        if arr:
            ans.append(arr)
        return ans



        