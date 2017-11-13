# python3
# 纯解题思路： 不再关心具体的增加操作，实际上二维数组当中操作最多的行数和列数相乘得到的就是最后的结果

class Solution(object):
    def maxCount(self, m, n, ops):
        if not ops:
                    return m*n
        return min([op[0] for op in ops])*min([op[1] for op in ops])