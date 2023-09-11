'''
设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。

实现 MinStack 类:

MinStack() 初始化堆栈对象。
void push(int val) 将元素val推入堆栈。
void pop() 删除堆栈顶部的元素。
int top() 获取堆栈顶部的元素。
int getMin() 获取堆栈中的最小元素。
'''
class MinStack(object):

    def __init__(self):
        self.stack = []


    def push(self, val):
        if self.stack and self.stack[-1][1] < val: self.stack.append((val, self.stack[-1][1]))
        else: self.stack.append((val, val))

    def pop(self):
        self.stack.pop()


    def top(self):
        return (self.stack[-1])[0]


    def getMin(self):
        return (self.stack[-1])[1]
