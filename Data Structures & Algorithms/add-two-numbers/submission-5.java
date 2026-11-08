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
        
        ListNode res = l1, dummy = new ListNode(), cur = dummy;
        int c = 0;
        while (l1 != null || l2 != null || c != 0) {
            int sum = (l1 != null ? l1.val : 0) + (l2 != null ? l2.val : 0) + c;
            c = sum / 10;

            cur.next = new ListNode(sum%10);
            c = sum/10;

            l1 = l1 != null ? l1.next : l1;
            l2 = l2 != null ? l2.next : l2;
            cur = cur.next;
        }

        return dummy.next;
    }
}
