# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class MyHashSet(object):
    """ Uses a linked list to make a hash set (slower than using an actual set) """

    def __init__(self):
        self.head = None
        self.tail = None
        

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        new_node = ListNode(key)

        if self.contains(key):
            # Don't add if the key exists: a set doesn't contain duplicates
            return

        if self.head is None:
            # Add the first node
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node  # Add to the end
            self.tail = new_node  # Update the tail


    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        current = self.head
        prev = None

        if current and current.val == key:
            # If the head is the key
            self.head = current.next
            if self.head is None:
                # Update tail if list becomes empty
                self.tail = None
            return

        while current:
            if current.val == key:
                prev.next = current.next
                if prev.next is None:
                    # Update tail if we removed the last node
                    self.tail = prev
                return
            prev = current
            current = current.next
        

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        current = self.head
        while current:
            if current.val == key:
                return True
            current = current.next
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)