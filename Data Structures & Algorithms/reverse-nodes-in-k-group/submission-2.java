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
    public ListNode reverseKGroup(ListNode head, int k) {
        
        ListNode prev = new ListNode(0);
        ListNode res = prev;

        int l = len(head);
        ListNode start = head;
        for (int i=0; i<l/k; i++) {
            prev.next = reverse(start, k);
            prev = start;
            start = start.next;
        }
        
        if (l%k != 0) prev.next = start;

        return res.next;
    }

    private ListNode reverse(ListNode head, int k) {

        ListNode prev=null, cur=head, next=null;

        for (int i=0; i<k; i++) {
            next = cur.next;
            cur.next = prev;
            prev = cur;
            cur = next;
        }
        head.next = cur;
        return prev;
    }

    private int len(ListNode n) {
        int l=0;

        while (n != null) {
            n = n.next;
            l++;
        }

        return l;
    }
}
