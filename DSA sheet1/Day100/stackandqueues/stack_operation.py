# """Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
#
# Implement the MinStack class:
#
# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# You must implement a solution with O(1) time complexity for each function."""
#
# class MinStack:
#     def __init__(self):
#         self.stack = []
#         self.mins = []
#
#     def push(self,value:int)->None: #push the element in to the stack and also compare each element in to stack such that min stack contain min value of the stack
#
#         self.stack.append(value)
#
#         if not self.mins or value <= self.mins[-1]:
#             self.mins.append(value)
#
#     def pop(self) -> None: #pop the element from the stack and also check the min stack should contain element is alo pop from that
#
#         if self.stack[-1] == self.mins[-1]:
#             self.mins.pop()
#         self.stack.pop()
#
#     def top(self) -> int:
#         return self.stack[-1] # Return the top element of stack
#
#     def getMin(self) -> int:
#         return self.mins[-1] # Return the top element of min_stack
#
# value=MinStack()
# value.push(4)
# value.push(5)
# value.push(8)
# value.push(2)
# print(value.getMin())
# print(value.pop())
# print(value.top())
#


class StackOperation:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        self.max_stack = []
    #
    # def push(self, item):
    #     self.stack = item + self.stack
    #     if len(self.min_stack) <=0 or item <= self.min_stack[-1]:
    #         self.min_stack.pop()
    #         self.min_stack = [item] + self.min_stack
    #     if len(self.max_stack) <=0 or item >= self.max_stack[-1]:
    #         self.max_stack.pop()
    #         self.max_stack = [item] + self.max_stack
    #
    # def pop(self,item):
    #     if self.stack[0] == self.min_stack[-1]:
    #         return self.min_stack.pop()
    #     return self.stack.pop()


    def push(self, item):
        self.stack.append(item)
        item = min(item, self.min_stack[-1] if self.min_stack else item)
        self.min_stack.append(item)
    def pop(self):
        value=self.stack.pop()
        if self.stack[-1] == value:self.min_stack.pop()

    def top(self):
        value=self.stack[-1]
        return value
    def get_min(self):
        return self.min_stack[-1]



value=StackOperation()
value.push(4)
value.push(5)
value.push(8)
value.push(2)
print(value.get_min())
print(value.pop())
print(value.top())
#
























