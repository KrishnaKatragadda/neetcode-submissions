# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return None
        slow = head
        fast = head.next
        ## Finding the middle of the linked list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        ## taking the second half of the list separate
        second = slow.next
        slow.next = None ## breaking it from first half

        ## now we need to reverse the list
        prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        ## List is reversed
        first,second = head,prev

        while second: ## usually second half is smaller
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2
        


        