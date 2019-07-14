#!python3
class Solution:
    # https://leetcode.com/problems/heaters/discuss/95875/Short-Python
    # short python
    # Time O(M+N) M 为heaters N为houses Space O()
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters = sorted(heaters) + [float("inf")]
        i = r = 0
        for x in sorted(houses):
            while x >= (heaters[i] + heaters[i+1]) / 2:
                i += 1
            r = max(r, abs(heaters[i] - x))
        return r
