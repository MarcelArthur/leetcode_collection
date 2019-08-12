#!python3
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # awesome 
        # https://www.youtube.com/watch?v=Up8iyOrq-5Y
        k = {v: i for i, v in enumerate(arr2)}
        return sorted(arr1, key=lambda i: k.get(i, 1000+i))
    
