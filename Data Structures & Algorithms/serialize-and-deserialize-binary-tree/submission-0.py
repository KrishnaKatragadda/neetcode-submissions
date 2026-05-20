# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        q = deque([root])
        res =[] ## using BFS to serialise the Tree

        while q:
            level = len(q)
            for i in range(level):
                temp = q.popleft()
                if temp:
                    res.append(str(temp.val))
                    #s = s+str(temp.val)+"#"
                    q.append(temp.left)
                    q.append(temp.right)
                else:
                    res.append("N")
                    #s = s+str(None)+"#"
        
        print(res)
        return ",".join(res)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        vals = data.split(",")
        root = TreeNode(int(vals[0]))
        q = deque([root])
        i = 1 ## to track the indices of the serialised string array
        while q:
            node = q.popleft()

            ## for left node
            if vals[i]!='N':
                node.left = TreeNode(int(vals[i]))
                q.append(node.left)
            i+=1

            ## for right node
            if vals[i]!='N':
                node.right = TreeNode(int(vals[i]))
                q.append(node.right)
            i+=1
        

        return root