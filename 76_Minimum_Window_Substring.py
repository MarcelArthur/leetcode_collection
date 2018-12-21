oimport collections 
class Solution:
    # def minWindow(self, s, t):
    #     """
    #     :type s: str
    #     :type t: str
    #     :rtype: str
    #     """
        # Solution 1: 先找到最小窗口的最右端的位置，再找到左端移动位置后即发生不满足要求的前一个位置，反馈对应两个位置截取的字符串。字典记录T字符串中字符的增减情况,记录符合条件的最短字符串的值。
#         res = ''
#         t_size = len(t)
#         mapping = {}
#         left, cnt, minlen = 0, 0, float('inf')
#         for i in t:
#             mapping[i] = mapping.get(i, 0) + 1
#         # 初始化mapping存储字符串T出现的字母次数
        
#         for j in range(len(s)):
#             mapping[s[j]] = mapping.get(s[j], 0) - 1
#             if mapping.get(s[j]) >= 0:
#                 cnt += 1
#             while cnt == t_size:
#                 if minlen > j - left + 1:
#                     minlen = j - left + 1
#                     res = s[left:minlen]
#                 mapping[s[left]] = mapping.get(s[left]) + 1
#                 if mapping[s[left]] > 0:
#                     cnt -= 1
#                 left += 1
#         return res
    
#     def minWindow(self, s, t):
#         res = ''
#         left, cnt, minlen = 0, 0, float('inf')
#         mapping = collections.Counter(t)
#         # 初始化mapping存储字符串T出现的字母次数
        
#         for j in range(len(s)):
#             mapping[s[j]] -= 1
#             if mapping[s[j]] >= 0:
#                 cnt += 1
#             while cnt == len(t):
#                 if minlen > j - left + 1:
#                     minlen = j - left + 1
#                     res = s[left:j + 1]
#                 mapping[s[left]] += 1
#                 if mapping[s[left]] > 0:
#                     cnt -= 1
#                 left += 1
#         return res
    
    # Solution 2: 由字典改为128长度的int列表进行判断，通过记录比对对应位置字符出现的次数进行最短字符串判断,依然是先找到最右边界，之后确认最合适左边界，获得最短字符串，虽然只改了结构，但是比原来快了很多。
    def minWindow(self, s, t):
        res = ''
        left, cnt, minlen = 0, 0, float('inf')
        mapping = [0 for x in range(128)] # 隐含“A-Z”在ASCII的前128位中
        for i in t:
            mapping[ord(i)] += 1
        # 初始化mapping存储字符串T出现的字母次数
        
        for j in range(len(s)):
            mapping[ord(s[j])] -= 1
            if mapping[ord(s[j])] >= 0:
                cnt += 1
            while cnt == len(t):
                if minlen > j - left + 1:
                    minlen = j - left + 1
                    res = s[left:j + 1]
                mapping[ord(s[left])] += 1
                if mapping[ord(s[left])] > 0:
                    cnt -= 1
                left += 1
        return res
        
        
