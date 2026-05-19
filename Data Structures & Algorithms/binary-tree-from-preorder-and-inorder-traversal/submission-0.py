# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        ## check if any of the given pre and inorder values list is None
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0]) ## The first element of the pre order list is always the Root value
        mid = inorder.index(preorder[0])
        ##### In inorder list, find the index of the root value. Everything towards the left of the root will be in left subtree and vice versa
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid]) ## passing the appropriate index values to the left subtree
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return root
        