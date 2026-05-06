# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head) ## create a dummy node and point it to head
        left = dummy
        right = head
        ## the right pointer will move by n places
        while n>0 and right:
            right = right.next
            n-=1
        
        while right:
            left = left.next
            right = right.next
        
        ## right reaches the end, left is at the Node before what needs to be deleted

        ## delete the node
        left.next = left.next.next

        return dummy.next
        

        