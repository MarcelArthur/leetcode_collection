class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.result = deque()
        for i in range(len(vec)):
            self.result.extend(vec[i])

    def next(self) -> int:
        return self.result.popleft()

    def hasNext(self) -> bool:
        if len(self.result) >= 1:
            return True
        return False


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()
