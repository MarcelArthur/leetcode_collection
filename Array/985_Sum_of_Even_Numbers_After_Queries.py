#!python3
class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        res_count = 0
        for n in A:
            if n % 2 == 0:
                res_count += n
        
        while queries:
            val, index = queries.pop(0)
            prev = A[index]
            A[index] = cur = A[index] + val
            if prev % 2 == 0 and cur % 2 == 0:
                res_count += val
            elif prev % 2 == 0:
                res_count -= prev
            elif cur % 2 == 0:
                res_count += cur
            res.append(res_count)
        return res
    
# simple Solution
class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
    	S, Q = sum([i for i in A if i % 2 == 0]), []
    	for [v,i] in queries:
    		a = A[i]
    		A[i] += v
    		if a % 2 == 0:
    			if v % 2 == 0: S += v
    			else: S -= a
    		elif v % 2 == 1: S += A[i]
    		Q.append(S)
    	return Q
