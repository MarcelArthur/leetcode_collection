class Solution:
    def maskPII(self, S):
        """
        :type S: str
        :rtype: str
        """
        
        '''
        首先需要通过首字母判断是邮箱还是手机号，再通过手机号逆置计数和邮箱分割方式快速组合结果(计数大于10则判断为需要加区号)
        没了 = = 默默水一题 溜了
        '''
        flag = 1
        if S[0] in '()1234567890+-':
            flag = 0
        const_str = '***-***-'
        if flag == 0:
            cnt = 0 
            res = ''
            for i in range(len(S) - 1, -1, -1):
                if S[i] in '1234567890':
                    cnt += 1
                    if cnt <= 4:
                        res += S[i]
            if cnt == 10:
                return const_str + res[::-1]
            else:
                return '+' + '*' * (cnt - 10) + '-' + const_str + res[::-1]
        if flag == 1:
            S = S.lower()
            left, right = S.split('@')
            return left[0] + '*****' +left[-1] + '@' + right
            
                
                    
                        
             
