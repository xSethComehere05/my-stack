class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack.pop()

    
    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)

S = Stack()
print("Is empty?:", S.is_empty())
for i in range(1,6):
    S.push(i)

print("Size after push:")
print("Top element:", S.peek())

print("Pop:", S.pop())
print("Pop:", S.pop())
print("Pop:", S.pop())
print("Pop:", S.pop())
print("Pop:", S.pop())

print("Is empty?:", S.is_empty())
print("Pop from empty", S.pop())