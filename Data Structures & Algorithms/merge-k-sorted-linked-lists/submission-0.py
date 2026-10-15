# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ##ok, so the approach is to start merging two lists at a time
        ## we need to slice up the list of lists into two list and mergethem 
        ## we continure this process until we have one big list left in the results

        if len(lists)==0: return None ## if its empty
        if not lists: return None

        while len(lists)>1: ## we repeat the compaction process until we have one remaining
            mLists = []

            for i in range(0,len(lists),2): ## we are looping throguh the list to pair 2 lists
                l1 = lists[i]
                l2 = lists[i+1] if (i+1)<len(lists) else None

                mLists.append(self.mergeTwoLists(l1,l2)) ## this will have partially merged, but all elements        
                
            lists = mLists ## if this contains one there we are done
        
        return lists[0]

    def mergeTwoLists(self, l1,l2):

        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        tail.next = l1 if l1 else l2
        return dummy.next
