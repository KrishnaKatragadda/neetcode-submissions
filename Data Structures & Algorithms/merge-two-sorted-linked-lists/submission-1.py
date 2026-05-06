# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        ## creating a dummy node, when solving Linkedlist problems 
        ## help avoid many edge cases

        dummy = ListNode()
        tail = dummy

        curr1, curr2 = list1, list2

        while curr1 and curr2:
            if curr1.val < curr2.val:
                tail.next = curr1
                curr1 = curr1.next
            else:
                tail.next = curr2
                curr2 = curr2.next
            tail = tail.next
        
        if curr1: ## if there are still pending elements in list
            tail.next = curr1 ## add them to the end of the new linked list
        elif curr2:
            tail.next = curr2
        
        return dummy.next
    