#!python3
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        res = collections.Counter(A[0])
        for i in range(1, len(A)):
            res &= collections.Counter(A[i])
        return list(res.elements())

class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        check = list(A[0])
        for word in A[1:]:
            new_check = []
            for c in word:
                if c in check:
                    new_check.append(c)
                    check.remove(c)
            check = new_check
        return check
    
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        res = set(A[0])
        result = [[l] * min([x.count(l) for x in A]) for l in res]
        return sorted([i for y in result for i in y])
