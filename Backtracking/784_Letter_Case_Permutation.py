#!python3
# 大佬写法
class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        L = [[i.lower(), i.upper()] if i.isalpha() else i for i in S]
        return [''.join(i) for i in itertools.product(*L)]
    

# BFS
class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        res = [""]
        for v in S:
            if v.isalpha():
                res = [i+j for i in res for j in [v.upper(), v.lower()]]
            else:
                res = [ch+v for ch in res]
        return res
