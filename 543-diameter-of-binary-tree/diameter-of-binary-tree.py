# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        res = 0
        def dfs(root, h):
            nonlocal res
            if not root:
                return h
            left = dfs(root.left, h)
            right = dfs(root.right, h)
            res = max(res, left +right)
            return 1 + max(left, right)
        dfs(root, 0)
        return res