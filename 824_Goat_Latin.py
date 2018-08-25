# Easy
class Solution:
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        # 预处理 这里通常还可以添加个判断函数去处理不同的数据类型
        S_list = S.split(' ')
        vowel = ['a', 'e', 'i', 'o', 'u']
        vowel.extend([x.upper() for x in vowel])
        
        for i in range(len(S_list)):
            if S_list[i][0] in vowel:
                S_list[i] += 'ma' + (i + 1) * 'a'
            else:
                S_list[i] = S_list[i][1:] + S_list[i][0] + 'ma' + (i + 1) * 'a'
        
        return ' '.join(S_list)
                
