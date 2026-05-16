# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def isGreat(node,val):
            if not node:
                return 0
            count = 0
            if node.val >= val:
                count=1
                val = node.val

            return (count+isGreat(node.left, val)+isGreat(node.right, val))
        return isGreat(root,float('-inf'))
            