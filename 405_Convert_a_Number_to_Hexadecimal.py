#!python3
class Solution:
    def toHex(self, num: int) -> str:
        Hex_dict = {10: "a", 11: "b", 12: "c", 13: "d", 14: "e", 15: "f"}

        if num == 0:
            return "0"

        if num < 0:
            num = num + 2 ** 32

        stack = list()
        while num > 0:
            rem = num % 16

            if num < 10:
                stack.append(rem)
            else:
                stack.append(Hex_dict[rem])

            num = num // 16
        return "".join(stack[::-1])
