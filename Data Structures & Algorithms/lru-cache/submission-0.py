class Node:
    def __init__(self,key, value):
        self.key, self.val = key, value
        self.next = self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity

        self.cache = {} ## this is used to key to Node

        ## Left = LRU, right = most recent
        self.left, self.right = Node(0,0),Node(0,0)
        self.left.next, self.right.prev = self.right, self.left
    
    def remove(self, node):
        prev,nxt = node.prev, node.next
        prev.next, nxt.prev = nxt,prev
    
    def insert(self, node):
        ## always insert at the right most
        prev = self.right.prev
        prev.next = self.right.prev = node
        node.next,node.prev = self.right,prev


    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key]) ## Node can be deleted from anywhere in the List
            ## It can be random, where Double LL helps
            self.insert(self.cache[key]) ## it should always be inserted at right
            ## THis helps keep the order and anything that is pointed by
            ## Left Node is LRU
            return self.cache[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        ## after the recent addition, check if the capacity is exceeded

        if len(self.cache) > self.cap:
            lru = self.left.next

            self.remove(lru) ## removing the node from LL

            del self.cache[lru.key] ## remove it from hash map
        
