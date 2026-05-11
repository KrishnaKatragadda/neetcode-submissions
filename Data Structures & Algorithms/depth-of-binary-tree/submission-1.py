# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: ## if the root, we are referring to is none, depth it will have 
        ## along the path is 0
            return 0
        
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return 1+max(left,right)
        