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
    public ListNode removeNthFromEnd(ListNode head, int k) {

        ListNode n = head;
        for (int i=0; i<k; i++) {
            n = n.next;
        }

        ListNode cur = head, prev = null;

        while (n != null) {
            prev = cur;
            cur = cur.next;
            n = n.next;
        }

        if (prev == null) return head.next;

        prev.next = prev.next.next;

        return head;
    }
}
