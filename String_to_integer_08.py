# -*- coding:utf-8 -*-

# 难度在LeetCode属于Easy难度
# 关键内置函数 (1) isdigit 判断容器中是否所有元素都为数字 (2) 判断多符号时只处理第一个符号剩下的符号不处理,判定为异常数字为0
# 处理字符串为数值的atoi方法


class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        result = 0
        # null of empty string
        if len(str) == 0:
            return 0

        # whitespaces
        str = str.lstrip()

        # +/- sign
        tmp = '0'
        i = 0
        if str[0] in "+-":
            tmp = str[0]
            i = 1

        # calcuate real value
        for j in range(i, len(str)):
            if str[j].isdigit():
                tmp += str[j]
            else:
                break

        if len(tmp) > 1:
            result = int(tmp)
        if result > INT_MAX:
            return INT_MAX
        elif result < INT_MIN:
            return INT_MIN
        else:
            return result


if __name__ == "__main__":
    str = '+-2'
    Cot = Solution()
    kt = Cot.myAtoi(str)
    print(kt)