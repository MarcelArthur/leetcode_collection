import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Solution 1:
            1. 构建不同字符的映射表
            2. 通过translate函数把对应编码的字符串替换掉,最终转换成小写
        Solution 2:
            正则匹配替换 re.sub('[^0-9a-zA-Z]+', '', s) 
        Solution 3:
            isalnum 判断非数字和字母
        string.punctuation 表示所有的标点字符 
        """ 
        # Solution 1
        punc = string.punctuation + ' '
        repl = str.maketrans(dict.fromkeys(punc, ''))
        s2 = s.translate(repl).lower()
        return s2 == s2[::-1]
    
        # Solution 2
        new_s = re.sub('[^0-9a-zA-Z]+','', s)
        print(new_s)
        new_s = new_s.lower()
        return new_s == new_s[::-1]
    
        # Solution 3:
        result = []
        for i in s:
            if i.isalnum():
                result.append(i.lower())
        res_s = "".join(result)
        return res_s == res_s[::-1]
                
