# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        while root:

            ### this is a BST - Binary search tree, all value in left subtree are less than root and same for right.

            if p.val <root.val and q.val <root.val: ## both the nodes are less than root. so LCA is in left
                root = root.left
            
            elif p.val > root.val and q.val > root.val:
                root = root.right   ## both the nodes are greater than root, so LCA is in right
            else:
                return root ## one is less and other is greater than root is the LCA
        