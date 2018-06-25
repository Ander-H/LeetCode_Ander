"""
https://leetcode.com/problems/implement-queue-using-stacks/description/
"""
class MyQueue:

    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x):
        self.input.append(x)

    def pop(self):
        self.move()
        return self.output.pop()

    def peek(self):
        self.move()
        return self.output[-1]

    def empty(self):
        return self.input == [] and self.output == []

    def move(self):
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()