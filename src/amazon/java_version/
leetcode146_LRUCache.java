

/* Implemented with built-in LinkedHashMap data structure */

public class LRUCache {

    private final int CAPACITY;
    private Map<Integer, Integer> cache;

    public LRUCache(int capacity) {
        CAPACITY = capacity;
        cache = new LinkedHashMap<Integer, Integer>(CAPACITY, 0.75f, true) {

            protected boolean removeEldestEntry(Map.Entry<Integer, Integer> eldest) {
                return size() > CAPACITY;
            }

        };
    }

    public int get(int key) {
        return this.cache.getOrDefault(key, -1);
    }

    public void put(int key, int value) {
        this.cache.put(key, value);
    }
}


/* Implemented with doubly linked list and HashMap */
public class LRUCache {
    
    private class ListNode {
        private int key;
        private int value;
        private ListNode prev;
        private ListNode next;
        
        ListNode() {
            this(0, 0);
        }
        
        ListNode(int key, int value) {
            this.key = key;
            this.value = value;
        }
        
        public int getKey() {
            return this.key;
        }
        
        public int getValue() {
            return this.value;
        }
        
        public void setValue(int value) {
            this.value = value;
        }
    }
    
    private final int CAPACITY;
    private Map<Integer, ListNode> hash;
    private ListNode head;
    private ListNode tail;
    
    public LRUCache(int capacity) {
        CAPACITY = capacity;
        this.hash = new HashMap<Integer, ListNode>();
        this.head = new ListNode();
        this.tail = new ListNode();
        this.head.next = this.tail;
        this.tail.prev = this.head;
    }
    
    public int get(int key) {
        if (this.hash.containsKey(key)) {
            ListNode node = this.hash.get(key);
            this.remove(node);
            this.append(node);
            return node.getValue();
        }
        return -1;
    }
    
    public void put(int key, int value) {
        if (CAPACITY > 0) {
            ListNode node;
            if (this.hash.containsKey(key)) {
                node = this.hash.get(key);
                node.setValue(value);
                this.remove(node);
                this.append(node);
            } else {
                if (this.hash.size() == CAPACITY) {
                    node = this.head.next;
                    this.hash.remove(node.key);
                    this.remove(node);
                    
                    node = new ListNode(key, value);
                    this.hash.put(key, node);
                    this.append(node);
                } else {
                    node = new ListNode(key, value);
                    this.hash.put(key, node);
                    this.append(node);
                }
            }
        }
    }
    
    private void append(ListNode node) {
        ListNode before = this.tail.prev;
        node.prev = before;
        node.next = this.tail;
        before.next = node;
        this.tail.prev = node;
    }
    
    private void remove(ListNode node) {
        ListNode before = node.prev;
        ListNode after = node.next;
        before.next = after;
        after.prev = before;
    }
}