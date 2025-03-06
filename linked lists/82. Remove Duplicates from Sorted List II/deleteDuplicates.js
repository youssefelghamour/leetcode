class ListNode {
    constructor(val = 0, next = null) {
      this.val = val;
      this.next = next;
    }
  }
  
  var deleteDuplicates = function(head) {
    let curr = head;
    let prev = null;
  
    while (curr && curr.next) {
      if (curr.val === curr.next.val) {
        let tmp = curr;
        let v = tmp.val;
  
        // Skip duplicates
        while (tmp && tmp.val === v) {
          tmp = tmp.next;
        }
  
        if (prev) {
          prev.next = tmp;
        } else {
          head = tmp;
        }
  
        curr = tmp;
      } else {
        prev = curr;
        curr = curr.next;
      }
    }
  
    return head;
  };
  