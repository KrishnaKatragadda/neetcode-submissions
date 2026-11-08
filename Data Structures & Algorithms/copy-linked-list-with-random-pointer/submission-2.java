/*
// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}
*/

class Solution {
    public Node copyRandomList(Node head) {
        
        Node cur = head;
        while (cur != null) {
            Node next = cur.next;
            cur.next = new Node(cur.val);
            cur.next.next = next;
            cur.next.random = cur.random;
            cur = next;
        }

        cur = head;
        while (cur != null) {
            Node next = cur.next.next;
            Node copyNode = cur.next;
            copyNode.random = cur.random != null ? cur.random.next : null;
            cur = next;
        }

        cur = head;
        Node res = head == null ? null : head.next;
        while (cur != null) {
            Node next = cur.next.next;
            Node copyNode = cur.next;
            cur.next = next;
            copyNode.next = next != null ? next.next : null;
            cur = next;
        }

        return res;
    }
}
