class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        '''
        考虑几种异常情况下的分析即可
        1 break_statu 标识出现未匹配的前缀字母情况
        2 pre记录首次记录的第一个前缀字母之后依次对比
        3 count 记录符合要求的值，满足则添加到最终结果res中
        特别注意: 需要避免位置超出每个单词的长度，如果超出则返回认为前缀字母已经搜索完成了
        '''
        if not strs:
            return ""
        if len(strs) < 2:
            return strs[0]
        break_statu = True
        n = 0
        
        result = ''
        while break_statu:
            count = 0
            pre = None
            for one in strs:
                if one == "" or n >= len(one):
                    break_statu = False
                if pre == None:
                    pre = one[n]
                    count += 1
                elif pre == one[n]:
                    count += 1
                else:
                    break_statu = False
            if count == len(strs):
                result += pre
            n += 1
        return result
            
