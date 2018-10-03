class Solution:
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        '''
        解题思路:
        位置相同，字符相同，A加一
        位置相同，字符不同，B加一(这里注意如果位置相同，字符不同且不在正确的字符内则不操作)
        没什么说的主要使用hash表进行映射记录，judge.get(secret[i])小于0的话说明secret[i]在geuss中出现过，则judge[secret[i]]加1，B加一,如果judge.get(v)大于0则正相反，在secret中出现过,judge[v]加一,B加一，代码如下。
        '''
        # judge = dict()
        # A, B = 0, 0
        # for i, v in enumerate(guess):
        #     if v == secret[i]:
        #         A += 1
        #     else:
        #         judge[secret[i]] = judge.get(secret[i], 0)
        #         judge[v] = judge.get(v, 0) 
        #         if judge.get(secret[i], 0) < 0:
        #             B += 1
        #         judge[secret[i]] += 1
        #         if judge.get(v, 0) > 0:
        #             B += 1
        #         judge[v] -= 1
        # return '{0}A{1}B'.format(A, B)
    
        # 简洁的三行代码 AC 90 %
#         bulls = sum(map(operator.eq, secret, guess))
#         both = sum(min(secret.count(x), guess.count(x)) for x in set(guess))
        
#         return str(bulls) + 'A' + str(both - bulls) + 'B'
    
