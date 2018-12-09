from collections import deque
class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        """
        Solution 1:
        按照任务从多到少依次为每个块分配任务。我们这里假定，A一定能够符合距离下一个A的冷却时间为n,         那么跟在A后面的也一定符合。只要保证A符合就行了，其他任务的的符合要求都可以由A的符合推导出来。
        c[25]是出现最多的字母数，所以(c[25] - 1)是分块数,例如A（4）次数最多，间隔n（3）(A***A***A***A)则重复的段落数为4-1=3。间隔是n，包含领头的A在内，每个间隔的长度是n+1=3+1=4.
        所以整个段落长度是(c[25] - 1) * (n + 1)。因为出现频率最高的元素可能不止一个，我们假设为k个，那么这种情况下最终的时间需求为：(c[25]-1)*（n+1）+k
        """
        
        maxFreq, maxFreqCount=0, 0
        f = [0 for x in range(26)] 
        freq = deque(f, maxlen=26)
        for taskone in tasks:
            freq[ord(taskone) - ord('A')] += 1
        for i in range(26):
            if freq[i] > maxFreq:
                maxFreq = freq[i]
                maxFreqCount = 1
            elif freq[i] == maxFreq:
                maxFreqCount += 1
        
        return max(len(tasks), (maxFreq - 1) * (n + 1) + maxFreqCount) 
