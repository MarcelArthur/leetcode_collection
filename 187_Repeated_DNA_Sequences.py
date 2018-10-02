class Solution:
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        '''
        1 字符串处理
        hashset判重和结果去重,标识10位长度的字符串出现过次数 > 1且结果不重复
        2 bit muliaption标识
        bit二进制逻辑判断-位操作去重/判断类题型(优点是节约空间)
        空间复杂度下降,效率更高
        Bit Manipulation
        由于我们的目的是利用位来区分字符，当然是越少位越好，通过观察发现，每个字符的后三位都不相同，故而我们可以用末尾三位来区分这四个字符。而题目要求是10个字符长度的串，每个字符用三位来区分，10个字符需要30位，在32位机上也OK。为了提取出后30位，我们还需要用个mask，取值为0x7ffffff，用此mask可取出后27位，再向左平移三位即可。算法的思想是，当取出第十个字符时，将其存在哈希表里，和该字符串出现频率映射，之后每向左移三位替换一个字符，查找新字符串在哈希表里出现次数，如果之前刚好出现过一次，则将当前字符串存入返回值的数组并将其出现次数加一，如果从未出现过，则将其映射到1。为了能更清楚的阐述整个过程，我们用题目中给的例子来分析整个过程：

首先我们取出前九个字符AAAAACCCC，根据上面的分析，我们用三位来表示一个字符，所以这九个字符可以用二进制表示为001001001001011011011，然后我们继续遍历字符串，下一个进来的是C，则当前字符为AAAAACCCCC，二进制表示为001001001001011011011011，然后我们将其存入哈希表中，用二进制的好处是可以用一个int变量来表示任意十个字符序列，比起直接存入字符串大大的节省了内存空间，然后再读入下一个字符C，则此时字符串为AAAACCCCCA，我们还是存入其二进制的表示形式，以此类推，当某个序列之前已经出现过了，我们将其存入结果res中即可.
        上面的方法都是用三位来表示一个字符，这里我们可以用两位来表示一个字符，00表示A，01表示C，10表示G，11表示T，那么我们总共需要20位就可以表示十个字符流，其余的思路跟上面的方法完全相同，注意这里的mask只需要表示18位，所以变成了0x3ffff，参见代码如下：
        '''
        res = set()
        judge_set = set()
        cur, i = 0, 0
        DNA_map = {
            'A': 0,
            'C': 1,
            'G': 2,
            'T': 3
        }
        while i < 9 and i < len(s):
            cur = (cur << 2) | (DNA_map[s[i]])
            i += 1
            
        while i < len(s):
            cur = ((cur & 0x3ffff) << 2) | (DNA_map[s[i]])
            i += 1
            if cur in judge_set:
                res.add(s[i-10: i])
            else:
                judge_set.add(cur)
        return list(res)
        
        # 不节约空间,字符串集合判重
        # res = []
        # judge_set = set()
        # # if len(s) == 10:
        # #     res.append(s)
        # for i in range(len(s)-9):
        #     one = s[i:i + 10]
        #     if one in judge_set and one not in res:
        #         res.append(one)
        #     else:
        #         judge_set.add(one)
        # return res
        
