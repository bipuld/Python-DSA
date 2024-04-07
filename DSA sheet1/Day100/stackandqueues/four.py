class Stack:
    def __init__(self):
        self.q1 = []  # Primary queue for storing elements (LIFO order)
        self.q2 = []  # Temporary queue for assisting push operations

    def push(self, data):
        """Pushes an integer element onto the stack."""
        self.q2.append(data)  # Add element to temporary queue (FIFO)
        while self.q1:
            self.q2.append(self.q1.pop())  # Move existing elements to q2
        self.q1, self.q2 = self.q2, []  # Swap queues to maintain LIFO order

    def pop(self):
        """Pops and returns the element from the top of the stack, or -1 if empty."""
        if self.isEmpty():
            return -1
        return self.q1.pop(0)  # Remove and return the first element (top)

    def top(self):
        """Returns the element at the top of the stack without removing it, or -1 if empty."""
        if self.isEmpty():
            return -1
        return self.q1[0]  # Return the first element (top)

    def size(self):
        """Returns the current size of the stack."""
        return len(self.q1)

    def isEmpty(self):
        """Returns True if the stack is empty, False otherwise."""
        return not self.q1

# Example usage
stack = Stack()

operations = [
    (1, 13),
    (1, 47),
    (4, None),
    (5, None),
    (2, None),
    (3, None),
]

for query_type, data in operations:
    if query_type == 1:
        stack.push(data)
    elif query_type == 2:
        popped_element = stack.pop()
        print(popped_element if popped_element != -1 else "Stack is empty")
    elif query_type == 3:
        top_element = stack.top()
        print(top_element if top_element != -1 else "Stack is empty")
    elif query_type == 4:
        print(stack.size())
    elif query_type == 5:
        print(stack.isEmpty())
