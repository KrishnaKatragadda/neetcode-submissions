# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = [k] ## this acts as a global variable, to maintain the count
        ans = [0]

        def dfs(node):
            if not node:
                return
            
            dfs(node.left) ## go to the left most node

            if count[0]==1: ## check if the counter came down to 1
                ans[0]=node.val ## you found the value
            
            count[0] = count[0]-1 ## if not, decrease the counter

            if count[0]>0: ## check if you have already fount the value
                dfs(node.right)
        
        dfs(root)
        return ans[0]

        