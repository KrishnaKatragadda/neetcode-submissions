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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        
        ListNode res = l1, prev = null;
        int c = 0;
        while (l1 != null || l2 != null) {
            int sum = (l1 != null ? l1.val : 0) + (l2 != null ? l2.val : 0) + c;
            c = sum / 10;

            if (l1 == null) {
                l1 = new ListNode(sum%10);
                if (prev != null) prev.next = l1;
            } else {
                l1.val = sum%10;
            }

            prev = l1;
            l1 = l1 != null ? l1.next : l1;
            l2 = l2 != null ? l2.next : l2;

        }

        if (c != 0) {
            prev.next = new ListNode(c);
        }

        return res;
    }
}
