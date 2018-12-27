class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Solution 1:
        # 
        # num记录前一个数字，pre_op记录前一个操作符。因为乘除类型的运算有优先级，所以需要根据pre_op进行判断。所以会出现如下的情况:
        # pre_op等于'+',num直接入栈，等待下一操作数进入处理
        # pre_op等于'-',num求反入栈，等待下一操作数进入处理
        # pre_op等于'*',则从栈中立刻弹出一个数字和前一个数字相乘，等待下一操作数进入处理
        # pre_op等于'/',则从栈中立刻弹出一个数字和前一个数字相除，等待下一操作数进入处理
        
        # 由于Python进行负数运算的话,处理逻辑和正数不一样,所以需要特殊处理
        stack = []
        pre_op = '+'
        num = 0
        for i, each in enumerate(s):
            if each.isdigit():
                num = 10 * num + int(each)
            if i == len(s) - 1 or each in "+-/*":
                if pre_op == '+':
                    stack.append(num)
                elif pre_op == '-':
                    stack.append(-num)
                elif pre_op == '*':
                    stack.append(stack.pop() * num)
                elif pre_op == '/':
                    top = stack.pop()
                    if top < 0:
                        stack.append(int(top / num))
                    else:
                        stack.append(top // num)
                pre_op = each
                num = 0
        return sum(stack)

