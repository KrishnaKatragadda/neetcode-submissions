# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        ## when we need rightSideView, we need to do Level order traversal 
        ## we use BFS to do that
        q = deque()
        q.append(root)

        while q:
            qLen = len(q)
            level = []

            for i in range(qLen): ## loop through each level items
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
                
            if level:
                res.append(level[-1]) ## return only the right most element in the level
        
        return res
            

        