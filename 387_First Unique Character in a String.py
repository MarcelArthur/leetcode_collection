# !python3
# 经典的算法问题 快速查找字符串第一个不重复的字符位置 通过字符串的find()和rfind()方法 高速查找并且得到结果



class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = len(s)
        letters = 'abcdefghigklmnopqrstuvwxyz'
        for l in letters:
            ind = s.find(l)
            if ind != -1 and ind == s.rfind(l):
                res = min(res, ind)
        if res == len(s):
            return -1
        else:
            return res


if __name__ == '__main__':
    first = Solution()
    print(first.firstUniqChar('leetcode'))