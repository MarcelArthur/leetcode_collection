#!python3
class Solution:
    """
    这道题有点奇怪，明明用了额外空间，结果最后都是 less than 100%...
    """
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        # Time O(N) Space O(1) 速度不快
        if not arr:
            return 
        count = 0
        length = len(arr)
        while count < length:
            if arr[count] == 0:
                arr.pop(-1)
                if count == length - 1:
                    arr.append(0)
                else:
                    arr.insert(count+1, 0)
                count += 1
            count += 1
    
    def duplicateZeros(self, arr: List[int]) -> None:
        
        # Best Solution of Discuss
        # 标记0的数量，反向移动对应位置的数据，也挺有意思的
        # 效率同上
        if not arr:
            return
        zeros = arr.count(0)
        n = len(arr)
        for i in range(n-1, -1, -1):
            if i+zeros < n:
                arr[i+zeros] = arr[i]
            if arr[i] == 0:
                zeros -= 1
                if i+zeros < n:
                    arr[i+zeros] = 0
    
    def duplicateZeros(self, arr: List[int]) -> None:
        # Fastest solution
        # Time O(N) Space O(N)
        # three points
        if not arr:
            return
        index, start, end = 0, 0, len(arr) - 1
        num = arr[:]
        flag = False
        while start <= end:
            if num[index] == 0 and start < end:
                arr[start] = num[index]
                start += 1
                flag = True
            if flag:
                arr[start] = num[index]
            start += 1
            index += 1
        
