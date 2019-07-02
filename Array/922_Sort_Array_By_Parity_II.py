#!python3
class Solution:
    # 最初解法 不是最优解 Space O(N) Time O()
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        res = []
        left = 0
        right = 0
        index = len(A)
        for i in range(len(A)):
            if i % 2 == 0:
                while left < index:
                    if A[left] % 2 == 0:
                        res.append(A[left])
                        left += 1
                        break
                    left += 1
            else:
                while right < index:
                    if A[right] % 2 != 0:
                        res.append(A[right])
                        right += 1
                        break
                    right += 1
        return res
    
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        # Space O(N) Time O(N)
        arr = [None] * len(A)
        a = 0
        b = 1
        for i, v in enumerate(A):
            if v % 2 == 0:
                arr[a] = v
                a += 2
            else:
                arr[b] = v
                b += 2
        return arr
    # good idea 
    # https://leetcode.com/problems/sort-array-by-parity-ii/discuss/319267/(Python-O(n)-T-and-O(1)-S)-easy-to-understand-with-explanation.
    # 详细解释了这种解法: 
    # Space Time O(N) Space O(1)
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        i, j, L = 0, 1, len(A)
        while j < L:
            if A[j] % 2 == 0:
                A[i], A[j] = A[j], A[i]
                i += 2
            else:
                j += 2
        return A
