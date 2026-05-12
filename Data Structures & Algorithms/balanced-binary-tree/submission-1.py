# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        self.isvalid = True ## flag to store the validity

        def height(node):
            if not node:
                return 0
            
            left = height(node.left)
            right = height(node.right)

            if abs(left-right)>1: ## break the cycle, if the difference between left and right path is greater
                self.isvalid = False
            
            return 1+max(left,right) ## return the height of tree at the node
        height(root)

        return self.isvalid
        