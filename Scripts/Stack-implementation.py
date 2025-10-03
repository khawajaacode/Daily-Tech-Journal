class Stack:
    def __init__(self):
        self.stack = []

    # Push an element onto the stack
    def push(self, item):
        self.stack.append(item)

    # Pop the top element from the stack
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return "Stack Underflow"

    # Peek at the top element without removing it
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return "Stack is empty"

    # Check if the stack is empty
    def is_empty(self):
        return len(self.stack) == 0

    # Get the size of the stack
    def size(self):
        return len(self.stack)

    # Display the stack
    def display(self):
        print(self.stack)


# Example usage
s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.display()        # [10, 20, 30]
print(s.pop())     # 30
print(s.peek())    # 20
print(s.size())    # 2
