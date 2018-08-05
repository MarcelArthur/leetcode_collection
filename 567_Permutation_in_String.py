import itertools
class Solution:
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        # Solution1: 通过itertools.permutatios排列s1的所有可能性,遍历可能排列在s2中出现的情况,返回结果超时 TLE
        # Solution2: 排序后依次处理与s1长度相同的字符串，比对成功则返回True TLE (排序耗时，果然TLE了)
        # Solution3: 两个hash表, 首先比对s1长度为n1的情况下，各个字符出现的频次，如果频次相同，则认为s2中包含s1, 当在n1长度下未发现结果时，继续遍历s2剩余的长度,同时要保证空间内的数目是稳定的，每遍历一个新字符，原有存储位置处于最左侧的字符数要-1。(参考大佬实现) 原有C++实现为vector, python不能直接生成256的hash表(因为是动态的hash表结构)，所以扫过一次大量数据的case结构,组成类似vector的hash表结果内存溢出(尴尬的python字典实现方式消耗大量内存)。GG
        # 2018/08/05 未解决 等待更新
        # if len(s1) > len(s2):
        #     return False
        # s1 = ''.join(sorted(s1, key=str.lower))
        # for i in range(len(s2) - len(s1) + 1):
        #     temp = s2[i:i + len(s1)]
        #     temp = ''.join(sorted(temp, key=str.lower))
        #     if temp == s1:
        #         return True
        # return False
        n1 = len(s1)
        n2 = len(s2)
        if n1 > n2:
            return False
        hash_s1 = dict()
        hash_s2 = dict()
        
        for c in range(n2):
            hash_s1[s2[c]] = 0
            hash_s2[s2[c]] = 0 
        for i in range(n1):
            hash_s1[s1[i]] = hash_s1.get(s1[i], 0) + 1
            hash_s2[s2[i]] = hash_s2.get(s2[i], 0) + 1
        if hash_s1 == hash_s2:
            return True
        for j in range(n1, n2):
            hash_s2[s2[j]] = hash_s2.get(s2[j], 0) + 1
            hash_s2[s2[j-n1]] = hash_s2.get(s2[j-n1], 0) - 1
            print(hash_s1)
            print(hash_s2)
            if hash_s1 == hash_s2:
                return True
        return False
            
