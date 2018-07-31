# (1)个人解法 随机数+序列赋值可解
import random
class Solution:
    
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.origin = nums[:]
        self.output = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
    
        return self.origin
        

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        shuffle_len = len(self.output)
        for i in range(shuffle_len):
            j = random.randint(i, shuffle_len-1)
            self.output[i], self.output[j] = self.output[j], self.output[i]
        return self.output




# 社区高效算法: python特性，随机排序(噗 看来对特性理解不深刻啊 逃)
import random
class Solution:
    
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.output = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.output
    
    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        return sorted(self.output, key=lambda x: random.random())
            
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()

