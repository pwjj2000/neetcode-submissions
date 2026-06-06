# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        curr, ans = [], []
        if not root:
            return ans
        q = deque([(root, 0)])
        while q:
            node, l = q.popleft()
            if l > len(ans):
                ans.append(curr.copy())
                curr = []
            curr.append(node.val)
            if node.left:
                q.append((node.left, l+1))
            if node.right:
                q.append((node.right, l+1))
        if curr:
            ans.append(curr)
        return ans