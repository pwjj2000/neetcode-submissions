# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        index = inorder.index(preorder[0])
        left_tree = self.buildTree(preorder[1:1+index], inorder[:index])
        right_tree = self.buildTree(preorder[1+index:], inorder[index+1:])
        root.left, root.right = left_tree, right_tree
        return root