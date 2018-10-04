class Solution:
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        # 交换糖果问题，实际上是数组再分配必须为平均值问题，转化下思路就能解决。时间复杂度不能太高,而且要避免重复计算
        total, sum_A, set_B = sum(A + B), sum(A), set(B)
        total = total >> 1
        for i, v in enumerate(A):
            b = total - (sum_A - v)
            if b in set_B:
                return [v, b]
