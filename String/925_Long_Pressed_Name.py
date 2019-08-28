#!python3
class Solution(object):
    def isLongPressedName(self, name, typed):
        g1 = [(k, len(list(grp))) for k, grp in itertools.groupby(name)]
        g2 = [(k, len(list(grp))) for k, grp in itertools.groupby(typed)]
        if len(g1) != len(g2):
            return False

        return all(k1 == k2 and v1 <= v2
                   for (k1,v1), (k2,v2) in zip(g1, g2))



class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        # Tine O(M+N) Space O(1)
        i = 0 
        for j in range(len(typed)):
            if i < len(name) and name[i] == typed[j]:
                i += 1
            elif j == 0 and typed[j] != typed[j-1]:
                return False
        return i == len(name)
