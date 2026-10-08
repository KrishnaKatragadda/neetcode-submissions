# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(l,r):
            if not l and not r:
                return True
            elif not l or not r:
                return False 
            else:
                if l.val == r.val:
                    return isSameTree(l.left,r.left) and isSameTree(l.right,r.right)
        
        if not root :
            return False 
        elif isSameTree(root,subRoot):
            return True
        else:
            return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)

        