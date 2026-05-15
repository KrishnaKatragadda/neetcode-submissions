# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        ## here, we need to traverse through the Tree in Level order, BFS
        ## we implement BFS using dequeue

        q = deque()
        q.append(root)

        while q:
            qLen = len(q)
            level =[] ## will store the nodes at given level
            for i in range(qLen): ## iterate through all nodes at current level
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
                
            if level:
                res.append(level)
        
        return res

        
        