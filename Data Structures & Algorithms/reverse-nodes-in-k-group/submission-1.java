
class Solution {

    public ListNode reverseKGroup(ListNode head, int k) {
        ListNode prevHead = new ListNode(-1);
        ListNode prev = prevHead;

        int l = len(head);
        ListNode next = head;

        for (int i = 0; i < l / k; i++) {
            ListNode start = next;

            prev.next = rev(start, k);
            prev = start;

            next = start.next; // Next group's head
        }

        prev.next = next;

        return prevHead.next;
    }

    ListNode rev(ListNode n, int k) {
        ListNode prev = null, cur = n;

        for (int i = 0; i < k; i++) {
            ListNode nextNode = cur.next;
            cur.next = prev;
            prev = cur;
            cur = nextNode;
        }

        n.next = cur; // KEY CHANGE

        return prev;
    }

    int len(ListNode n) {
        int l = 0;
        while (n != null) {
            l++;
            n = n.next;
        }
        return l;
    }
}
