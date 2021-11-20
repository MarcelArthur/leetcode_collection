class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        poi1, poi2 = 1, 1
        n1, n2 = ord(num1[0]) - ord("0"), ord(num2[0]) - ord("0")
        while poi1 <= len(num1) - 1 or poi2 <= len(num2) - 1:
            if poi1 <= len(num1) - 1:
                v1 = num1[poi1]
                v1 = ord(v1) - ord("0")
                n1 = n1 * 10 + v1
                poi1 += 1
            if poi2 <= len(num2) - 1:
                v2 = num2[poi2]
                v2 = ord(v2) - ord("0")
                n2 = n2 * 10 + v2
                poi2 += 1
        return str(n1 * n2)
