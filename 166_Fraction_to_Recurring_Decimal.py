class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        sign = (numerator * denominator) >= 0
        numerator, denominator = abs(numerator), abs(denominator)
        
        q, r = divmod(numerator, denominator)
        
        res = str(q)
        if not sign:
            res = "-" + res
        
        if r == 0:
            return res
        
        l = []
        dic = {}
        r = r * 10
        while r != 0:
            tmp, r = divmod(r, denominator)
            if r in dic and tmp == dic[r][0]:
                break
            else:
                dic[r] = [tmp, len(l)]
            l.append(str(tmp))
            r *= 10
        
        res += "."
        if r == 0:
            return res + "".join(l)
        else:
            for i in range(len(l)):
                if i == dic[r][1]:
                    res += '('
                res += str(l[i])
            res += ')'
            return res
