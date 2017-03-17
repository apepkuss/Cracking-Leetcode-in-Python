
import java.util.*;

public class LFUCache {
    // capacity of LFUCache
    private int capacity = 0;
    // store key-value pair
    private Map<Integer, Integer> valueHash;
    // store key-node pair for maintaining LCU
    private Map<Integer, Node> nodeHash;
    // maintain a linked list based on node's frequency
    private Node head;

    public LFUCache(int capacity) {
        this.capacity = capacity;
        valueHash = new HashMap<Integer, Integer>();
        nodeHash = new HashMap<Integer, Node>();
    }

    public int get(int key) {
        if (!this.valueHash.containsKey(key))
            return -1;

        // increase frequency
        this.increaseFreq(key);
        return this.valueHash.get(key);
    }

    private void increaseFreq(int key) {
        Node node = this.nodeHash.get(key);
        node.keys.remove(key);

        if (node.next == null) {
            node.next = new Node(node.freq + 1);
            node.next.keys.add(key);
            node.next.prev = node;
        } else if (node.next.freq == node.freq + 1) {
            node.next.keys.add(key);
        } else {
            Node tmp = new Node(node.freq + 1);
            tmp.keys.add(key);
            tmp.prev = node;
            tmp.next = node.next;
            node.next.prev = tmp;
            node.next = tmp;
        }

        this.nodeHash.put(key, node.next);
        if (node.keys.size() == 0) this.remove(node);
    }

    public void put(int key, int value) {
        if (this.capacity == 0)
            return;

        if (this.valueHash.containsKey(key)) {
            this.valueHash.put(key, value);
        } else {
            if (this.valueHash.size() >= this.capacity) {
                this.removeEldest();
            }

            this.valueHash.put(key, value);
            this.addToHead(key);
        }
        this.increaseFreq(key);
    }

    private void removeEldest() {
        if (this.head == null)
            return;

        // get LCU key
        int key = 0;
        for (int k : this.head.keys) {
            key = k;
            break;
        }
        this.head.keys.remove(key);
        if (this.head.keys.size() == 0)
            this.remove(this.head);
        this.valueHash.remove(key);
        this.nodeHash.remove(key);
    }

    private void remove(Node node) {
        if (node.prev == null) {
            this.head = node.next;
        } else {
            node.prev.next = node.next;
        }

        if (node.next != null) {
            node.next.prev = node.prev;
        }
    }

    private void addToHead(int key) {
        if (this.head == null) {
            this.head = new Node(0);
            this.head.keys.add(key);
        } else if (this.head.freq > 0) {
            Node node = new Node(0);
            node.keys.add(key);
            node.next = this.head;
            this.head.prev = node;
            this.head = node;
        } else {
            this.head.keys.add(key);
        }

        this.nodeHash.put(key, this.head);
    }

    // Frequency Node stores all keys having same frequency value
    class Node {
        // frequency
        private int freq;
        // store keys in LCU order, which have same frequency
        private LinkedHashSet<Integer> keys;
        private Node prev;
        private Node next;


        public Node(int frequency) {
            this.freq = frequency;
            this.keys = new LinkedHashSet<Integer>();
            this.prev = null;
            this.next = null;
        }
    }
}



/**
 * Your LFUCache object will be instantiated and called as such:
 * LFUCache obj = new LFUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */