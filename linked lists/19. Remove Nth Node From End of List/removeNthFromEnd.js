/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} n
 * @return {ListNode}
 */
var removeNthFromEnd = function(head, n) {
    let len = 0;
    let node = head;
    
    while (node) {
        node = node.next;
        len++;
    }
    
    if (len === n) {
        return head.next;
    }
    
    node = head;
    for (let i = 0; i < len - 1 - n; i++) {
        node = node.next;
    }
    
    node.next = node.next.next;
    
    return head;
};