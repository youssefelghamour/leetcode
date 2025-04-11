  
class Solution {
    length(head) {
        let l = 0;
        while (head) {
            l++;
            head = head.next;
        }
        return l;
    }
  
    rotateRight(head, k) {
        let curr = head;
        let prev = null;
        let l = this.length(head);

        if (!head || !head.next) {
            return head;
        }

        if (k > l) {
            k = k % l;
        }

        for (let i = 0; i < k; i++) {
            curr = head;
            prev = null;

            while (curr && curr.next) {
                prev = curr;
                curr = curr.next;
            }

            prev.next = null;
            curr.next = head;
            head = curr;
        }

        return head;
    }
}  