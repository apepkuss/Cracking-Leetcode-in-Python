

/**
 * Definition for singly-linked list with a random pointer.
 * class RandomListNode {
 *     int label;
 *     RandomListNode next, random;
 *     RandomListNode(int x) { this.label = x; }
 * };
 */
public class Solution {
    public RandomListNode copyRandomList(RandomListNode head) {

        if (head == null) return null;

        // duplicate each node in current list
        RandomListNode p = head;
        while (p != null) {
            RandomListNode node = new RandomListNode(p.label);
            node.next = p.next;
            p.next = node;
            p = node.next;
        }

        // construct random pointer of each duplicated node
        p = head;
        while (p != null) {
            if (p.random != null) {
                p.next.random = p.random.next;
            }
            p = p.next.next;
        }

        // extract new list
        RandomListNode dummy = new RandomListNode(0);
        dummy.next = head.next;
        p = dummy;
        RandomListNode q = head;
        while (q != null) {
            p.next = q.next;
            q.next = q.next.next;
            q = q.next;
            p = p.next;
        }

        return dummy.next;
    }
}