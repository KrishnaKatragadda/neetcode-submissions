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

        head = new Node(0, 0);
        tail = new Node(0, 0);
        head.next = tail;
        tail.prev = head;
    }
    
    public int get(int key) {
        if (m.containsKey(key)) {
            Node n = m.get(key);
            remove(n);
            insert(n);
            return n.val;
        }
        return -1;
    }
    
    public void put(int key, int value) {
        if (m.containsKey(key)) {
            remove(m.get(key));
        }

        Node n = new Node(key, value);
        insert(n);
        m.put(key, n);

        if (m.size() > cap) {
            m.remove(tail.prev.key);
            remove(tail.prev);
        }
    }

    private void insert(Node n) {
        Node headNext = head.next;
        n.next = headNext;
        headNext.prev = n;
        n.prev = head;
        head.next = n;
    }

    private void remove(Node n) {
        
        Node nextNode = n.next;
        Node prevNode = n.prev;
        prevNode.next = nextNode;
        nextNode.prev = prevNode;
    }
}
