#!python3


class LinkedNode:
    def __init__(self, x):
        self.pre = None
        self.val = x
        self.next = None


class MyQueue:
    """
    双向链表实现
    """
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.linked_list = LinkedNode(None)
        self.Node  = self.linked_list
        self.Node.next = self.linked_list
        self.size = 0

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        if self.linked_list:
            node = LinkedNode(x)
            self.linked_list.next = node
            node.pre = self.linked_list
            self.linked_list = self.linked_list.next
        else:
            node = LinkedNode(x)
            self.linked_list = node
        self.size += 1
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.size:
            x = self.Node.next.val
            self.Node.next.pre = None
            self.Node = self.Node.next
            self.size -= 1
            return x
        return 

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.Node.next.val

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if self.size:
            return False
        return True
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
