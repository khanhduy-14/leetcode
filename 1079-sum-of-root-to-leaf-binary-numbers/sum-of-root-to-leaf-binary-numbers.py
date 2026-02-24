# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node: Optional[TreeNode], current: int) -> int:
        if not node:
            return 0
        current = current * 2 + node.val

        if not node.left and not node.right:
            return current
        
        return self.dfs(node.left, current) + self.dfs(node.right, current)

            
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, 0)
        