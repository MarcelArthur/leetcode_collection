# -*- coding:utf-8 -*-
# 求最短字符串中的值(多次遍历之后，找到最长字符串中的值并且打印)
# 使用KMP算法，标记出现过的元素的位置  KMP算法 GG++ 等想明白再写


class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        self.maxlen = 0
        self.retstr = ''
        if len(s) < 2:
            return s
        for i in range(len(s)):
            self.__find_palindrome(s, i, i) #奇回文
            self.__find_palindrome(s, i, i+1) #偶回文
        return self.retstr

    def __find_palindrome(self, s, j, k):
        while j >= 0 and k < len(s) and s[j] == s[k]:
            j -= 1
            k += 1
        if self.maxlen < k - j + 1:
            if j <= 0:
                if k == len(s) and s[k-1] == s[j+1]:
                    self.maxlen = k - j + 1
                    self.retstr = s[j + 1:]
                elif k == len(s):
                    self.maxlen = k - j + 1
                    self.retstr = s[len(s) - 1::-1] + s[j + 1:len(s)]
                else:
                    self.maxlen = k - j + 1
                    self.retstr = s[len(s)-1:k-1:-1]+s[j+1:len(s)]

if __name__ == "__main__":
    Short = Solution()
    Str = "aacecaaa"
    k = "abb"
    sor = Short.shortestPalindrome(k)
    print(sor)