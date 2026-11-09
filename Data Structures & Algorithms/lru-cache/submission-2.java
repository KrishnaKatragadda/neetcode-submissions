class LRUCache {

    int cap;
    Map<Integer, Node> m;
    Node head, tail;

    class Node {
        int val;
        int key;
        Node prev;
        Node next;

        Node(int k, int v) {
            key = k;
            val = v;
        }
    }

    public LRUCache(int capacity) {
        cap = capacity;
        m = new HashMap<>();
    }
    
    public int get(int key) {
        if (m.containsKey(key)) {
            Node n = m.get(key);
            moveToHead(n);
            return n.val;
        }

        return -1;
    }
    
    public void put(int key, int value) {
        Node n;
        if (m.containsKey(key)) {
            n = m.get(key);
            n.val = value;
        } else {
            n = new Node(key, value);
            if (m.size() == 0) {
                head = tail = n;
            }
            m.put(key, n);
        }
        moveToHead(n);
        if (m.size() > cap) removeTail();
    }

    private void moveToHead(Node n) {
        if (head == n) return;
        if (tail == n) {
            tail = tail.prev;
            tail.next = null;
        }
        Node prevNode = n.prev;
        Node nextNode = n.next;

        n.prev = null;
        n.next = head;
        head.prev = n;
        head = n;

        if (prevNode != null) prevNode.next = nextNode;
        if (nextNode != null) nextNode.prev = prevNode;
    }

    private void removeTail() {
        m.remove(tail.key);
        if (m.size() == 0) {
            head = tail = null;
            return;
        }
        Node prevNode = tail.prev;
        tail.prev = null;
        if (prevNode != null) prevNode.next = null;
        m.remove(tail.key);
        tail = prevNode;
    }
}
