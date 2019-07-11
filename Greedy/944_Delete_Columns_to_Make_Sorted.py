#!python3
class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        # 看懂题意也挺费事的
        # 保证每列字母都是递增关系，如果非递增则剔除，剔除该字符串
        if not A:
            return 0
        ans = 0
        n, m = len(A), len(A[0])
        for i in range(m):
            for j in range(1, n):
                if A[j-1][i] > A[j][i]:
                    ans += 1
                    break
        return ans
