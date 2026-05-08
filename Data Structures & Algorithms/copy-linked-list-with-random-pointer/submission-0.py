"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        ## create a hash map to associate old nodes in LL to new nodes created
        old = {None: None} ## handling the pointers pointing to NULL
        curr = head

        while curr:
            copy = Node(curr.val)
            old[curr] = copy
            curr = curr.next
        
        curr = head
        while curr:
            new = old[curr]
            new.next = old[curr.next]
            new.random = old[curr.random]
            curr = curr.next
        
        return old[head]