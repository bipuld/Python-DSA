# Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).
#
# Implement the MyStack class:
#
# void push(int x) Pushes element x to the top of the stack.
# int pop() Removes the element on the top of the stack and returns it.
# int top() Returns the element on the top of the stack.
# boolean empty() Returns true if the stack is empty, false otherwise.
#

class Stack:
    def __init__(self):
        self.queues1 = []
        self.queues2 = []


    def push(self,x):
            while self.queues1:
                self.queues2.append(self.queues1.pop(0))
            self.queues1.append(x)
            self.queues1, self.queues2 = self.queues2, self.queues1

    def pop(self):
        return self.queues1.pop(0)  # Directly pop from q1

    def top(self):
        return self.queues1[0]  # View the first element in q1

    def is_empty(self):
        return not self.queues1  # True if q1 is empty



myStack = Stack()
myStack.push(1);
myStack.push(2);
myStack.top();
myStack.pop();
myStack.is_empty();
