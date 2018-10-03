class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        1 第一思路 通过字段映射记录每个数字出现的次数(涉及操作读取,update次数,删除键 or 循环读取只出现过一次的数字key)
        不用问了 TL Note提示不是白写的orz
        2 位操作 下面是两种位操作实现 思路大同小异(主要是模拟三进制的过程,当记录次数结束的时候删除)
        '''
        # 
        # one = 0
        # two = 0
        # three = 0
        # for i in range(0,len(nums)):
        #     two |= one & nums[i] #当新来的为0时，two = two | 0，two不变，当新来的为1时，（当one此时为0，则two = two|0，two不变；当one此时为1时，则two = two | 1，two变为1
        #     one ^= nums[i]       #新来的为0，one不变，新来为1时，one是0、1交替改变
        #     three = one & two    #当one和two为1是，three为1（此时代表要把one和two清零了）
        #     one &= ~three        #把one清0
        #     two &= ~three        #把two清0
        # return one
        
        '''
        ur: https://blog.csdn.net/fuxuemingzhu/article/details/79554959
        这个题的做法是把32位的二进制数进行遍历，统计每个数字的每一位出现的和。因为每个数字出现了3次或者1次，所以如果某一位出现的次数不是3次，那么这个位置一定是因为那个只出现1次的数字导致的。用来保存结果的res是0，因此使用或操作，就能把这个位置的数字变成1.
        '''
        # res = 0
        # for i in range(32):
        #     cnt = 0
        #     mask = 1 << i
        #     for num in nums:
        #         if num & mask:
        #             cnt += 1
        #     if cnt % 3 == 1:
        #         res |= mask
        # if res >= 2**31:
        #     res -= 2**32
        # return res
        
        # 类似三进制求解的思路(第一次记录ones，第二次记录twos，第三次清空,最后只返回ones的值)
        ones,twos=0,0
        for ele in nums:
            ones = ones^ele & ~twos
            twos = twos^ele & ~ones
        return ones
        
        # 
        # 4 对不起这个是数学问题 c = (3 * set([a,b,c]) - sum([a,a,b,b,c])//2  AC 99%
        # return int((3*sum(list(set(nums)))-sum(nums))/2)

