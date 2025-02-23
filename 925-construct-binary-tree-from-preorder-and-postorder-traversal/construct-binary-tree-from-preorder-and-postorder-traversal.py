# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def makeTree():
            root = TreeNode(postorder.pop())
            if root.val != preorder[-1]:
                root.right = makeTree()
            if root.val != preorder[-1]:
                root.left = makeTree()
            
            preorder.pop()


            return root
        
        return makeTree()
        