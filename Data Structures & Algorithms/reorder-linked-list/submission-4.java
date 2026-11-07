/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public void reorderList(ListNode head) {
        
        ListNode s, f;
        s = f = head;

        while (f != null && f.next != null) {
            s = s.next;
            f = f.next.next;
        }
        
        // consider mid.next as the second list
        ListNode cur = s.next, prev = null, next = null;
        // make the end of first list null
        s.next = null;

        while (cur != null) {
            next = cur.next;
            cur.next = prev;
            prev = cur;
            cur = next;
        }

        ListNode head1 = head, head2 = prev;

        //we check if head2 is null beacuse head1 keep increasing
        while (head2 != null) {
            ListNode head1Next = head1.next;
            ListNode head2Next = head2.next;
            head1.next = head2;
            head2.next = head1Next;
            head1 = head1Next;
            head2 = head2Next;
        }

    }
}
