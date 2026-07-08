"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        new = {}
        new[node] = Node(node.val)
        q = deque([node])

        while q:
            curr = q.popleft()

            for n in curr.neighbors:
                if n not in new:
                    new[n] = Node(n.val)
                    q.append(n)
                
                new[curr].neighbors.append(new[n])

        
        return new[node]

