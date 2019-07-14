#!python3
class ListNode:
    def __init__(self, key, value):
        self.pair = (key, value)
        self.next = None
        

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.m = 1000
        self.h = [None] * self.m

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        index = self._hash(key)
        if self.h[index] is None:
            self.h[index] = ListNode(key, value)
        else:
            cur = self.h[index]
            while cur:
                if cur.pair[0] == key:
                    cur.pair = (key, value)
                    return
                if cur.next is None:
                    break
                cur = cur.next
            cur.next = ListNode(key, value)
        

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        index = self._hash(key)
        cur = self.h[index]
        while cur:
            if cur.pair[0] == key:
                return cur.pair[1]
            cur = cur.next
        return -1
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        index = self._hash(key)
        prev=cur=self.h[index]
        if not cur:
            return 
        if cur.pair[0] == key:
            self.h[index] = cur.next
        else:
            cur = cur.next
            while cur:
                if cur.pair[0] == key:
                    prev.next = cur.next
                    break
                else:
                    prev, cur = prev.next, cur.next
    
        
    def _hash(self, key):
        """
        Return key Hash for the self.h
        """
        return key % self.m


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
