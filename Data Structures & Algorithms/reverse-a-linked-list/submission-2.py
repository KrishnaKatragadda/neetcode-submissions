# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: ## if the linked list is empty, return None
            return None

        curr,prev = head, None ## declaring prev to store the previous Node

        while curr:
            temp = curr.next  ## pointer to the next node
            curr.next = prev
            prev = curr
            curr = temp
        
        return prev
        