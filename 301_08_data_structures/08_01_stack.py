# Build a custom `Stack` similar to the `Queue` you built


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.length = 0

    def is_empty(self):
        return self.head is None

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.head.value

    def push(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.length += 1

    def pop(self):
        if self.is_empty():
            return None
        else:
            popped_node = self.head
            self.head = self.head.next
            self.length -= 1
        return popped_node.value


daily_tasks = Stack()

daily_tasks.push("go to the gym")
daily_tasks.push("prepare breakfast")
daily_tasks.push("go to work")

print(f"Peeking: {daily_tasks.peek()}")

print(f"Completed: {daily_tasks.pop()}")
print(f"Completed: {daily_tasks.pop()}")