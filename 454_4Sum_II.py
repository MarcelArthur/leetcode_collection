from typing import List


class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:

        # 动规
        # Solution 1: Easy Solution 我们可以认为要使得和为0，我们需要使任意两个数产生的结果是互为相反数，因此可以很多得到解法 AC more than 26.38%
        # 缺点: 时间复杂度O(N^2)
        """
        sumber_dict = dict()

        for i in range(len(A)):
            for j in range(len(B)):
                if A[i] + B[j] in sumber_dict:
                    sumber_dict[A[i] + B[j]] += 1
                else:
                    sumber_dict[A[i] + B[j]] = 1

        count = 0

        for i in range(len(C)):
            for j in range(len(D)):
                if 0 - (C[i] + D[j]) in sumber_dict:
                    count += sumber_dict[0 - (C[i] + D[j])]
        return count
        """

        A_dict = {}

        for i in A:
            if i in A_dict:
                A_dict[i] += 1
            else:
                A_dict[i] = 1

        B_dict = {}

        for i in B:
            if i in B_dict:
                B_dict[i] += 1
            else:
                B_dict[i] = 1

        C_dict = {}

        for i in C:
            if i in C_dict:
                C_dict[i] += 1
            else:
                C_dict[i] = 1

        D_dict = {}

        for i in D:
            if i in D_dict:
                D_dict[i] += 1
            else:
                D_dict[i] = 1

        AB = {}

        for i in A_dict:
            for j in B_dict:
                if i + j in AB:
                    AB[i + j] += A_dict[i] * B_dict[j]
                else:
                    AB[i + j] = A_dict[i] * B_dict[j]

        count = 0

        for i in C_dict:
            for j in D_dict:
                if -i - j in AB:
                    count += C_dict[i] * D_dict[j] * AB[-i - j]

        return count


