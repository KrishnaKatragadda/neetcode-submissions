# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        if not subRoot:
            return True
        
        if self.sameTree(root,subRoot): ## check, at the given level is the tree are same
            return True
        return (self.isSubtree(root.left, subRoot)  or self.isSubtree(root.right, subRoot)) ## then pass subtree
        
    def sameTree(self, r,sb): ## code to check if the given two trees are same or not
        if not r and not sb:
            return True
        
        if r and sb and r.val == sb.val:
            return (self.sameTree(r.left, sb.left)  and self.sameTree(r.right, sb.right))
        
        return False
        