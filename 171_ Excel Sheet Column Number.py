# !python3
# 考察二十六进制的理解（非真正二十六进制），每次超过二十六都会有类似十进制的向前进位 这里居然卡了一段时间 早就想到了类似进制的
# 逻辑关系，不过没有得到具体的关系，一直绕在里面没有出来，思考不太好思考（囧...）
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        if not s:
            return result
        for i in range(len(s)):
            result += (ord(s[i]) - 64) * pow(26, len(s) - 1 - i)
        return result