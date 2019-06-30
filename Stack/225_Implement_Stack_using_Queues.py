#!python3
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._size = 0
        self._top = None
        self._list = []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self._list.append(x)
        self._size += 1
        self._top = x

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if self._size == 0:
            return
        self._list.remove(self._top)
        x = self._top
        self._top = self._list[-1] if self._list else None
        self._size -= 1
        return x

    def top(self) -> int:
        """
        Get the top element.
        """
        return self._top

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        if self._size:
            return False
        return True
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
