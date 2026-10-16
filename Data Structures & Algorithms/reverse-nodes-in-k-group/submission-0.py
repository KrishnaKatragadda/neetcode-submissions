# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        ## we need to first group the nodes into size k
        ## reverse the groups
        ## patch it back to the LL, continue further

        dummy = ListNode(0,head) ## create a dummy and point it to head

        ### we need 4 pointers,
        ## groupPrev and groupNext to indicate node before group and after group to link
        ## groupStart and kth to indicate start of the current group and end

        groupPrev = dummy ## node before 

        while True:
            kth = groupPrev

            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next ## at a point where there are no suff nodes to form a group, we reached end. so return the result
            ## we now have all 4 pointers ready
            groupStart = groupPrev.next
            groupNext = kth.next
## Now we can perform the reverse LL
            prev = groupNext
            curr = groupStart

            while curr!=groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
## now revers is completed, now we need to path it.
            groupPrev.next = kth
            groupPrev = groupStart