#!python3
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        f = [0] + flowerbed + [0]
        for i in range(1, len(f) - 1):
            if f[i] == f[i-1] == f[i+1]:
                n -= 1
                f[i] = 1
                if n == 0:
                    return True
        return False
