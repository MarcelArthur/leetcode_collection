#!python3
class Solution:
    def reachNumber(self, target: int) -> int:
        # Solution  https://www.cnblogs.com/grandyang/p/8456022.html
        # 解析: 根据题目观察得到当cur大于target且保证相差为偶数时为最小步数，另外对于target取绝对值不会影响最小步数
        target = abs(target)
        cur = 0
        i = 1
        while cur < target or (cur - target) % 2 == 1:
            cur += i
            i += 1
        return i - 1
