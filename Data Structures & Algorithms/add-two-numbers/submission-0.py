# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ## When the situation is to create a deep copy, create new linked list
        ## it is good practise to use Dummy pointer technique

        dummy = ListNode()
        curr = dummy

        ## defining carry to hold carry
        carry = 0 

        while l1 or l2 or carry:

            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            ## checking if the values are present or use 0

            val = v1+v2+carry

            ## check for new carry
            carry = val //10
            val = val %10

            ## creating new node with resultant value

            curr.next = ListNode(val)

            ## updating the pointers

            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
        